%{
#include "json-defs.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string pprint_json(json_map *);

void delete_json_map(json_map *object) {
	json_map_iterator i;
	for (i = object->begin(); i != object->end(); ++i)    {
	  delete i->second; // calls ~descriptor in json-defs.h, recursive deletes ensue
	}   
    delete object;
}

string comma_list(vector<string> &sv) {
    vector<string>::iterator i = sv.begin();
    string output;
    do {
        if (i != sv.begin()) output += ",";
        output += *i;
        ++i;
    } while ( i != sv.end() );
    return output;
}

// example of how to walk the json_map data structure that
// is built from the json file
string pprint_descriptor(descriptor *d) {
    vector<string> output;
    switch( d->type ) {
    // all the scalar values are kept as string values
    case D_STRING: 
    case D_NUMBER: 
    case D_BOOLEAN: 
    case D_NULL: 
        { 
            output.push_back(d->value);
            break; 
        }
    case D_ARRAY: 
        {   
            string array_str("[");
            json_array_iterator j;
            vector<string> array_output;
            for (j = d->array->begin(); j != d->array->end(); ++j) {
                array_output.push_back( pprint_descriptor(*j) );
            }   
            array_str += comma_list(array_output);
            array_str += "]";
            output.push_back(array_str);
            break; 
        }   
    case D_OBJECT: 
        {   
            output.push_back( pprint_json(d->object) );
            break;
        }   
    }
    return comma_list(output);
}

string pprint_json(json_map *object) {
    string object_str("{");
	json_map_iterator i;
    vector<string> object_output;
	for (i = object->begin(); i != object->end(); ++i) {
        string cur_object = i->first;
        cur_object += ":";
        cur_object += pprint_descriptor(i->second);
        object_output.push_back(cur_object);
	}
    object_str += comma_list(object_output);
    object_str += "}";
    return object_str;
}

void print_json(json_map *object) {
    cout << pprint_json(object) << endl;
}

%}

%union {
  string *s_val;
  json_map *object_val;
  json_array *array_val;
  descriptor *desc_val;
}

%token <s_val> T_STR T_NUM T_BOOL T_NULL
%type <object_val> object object_content keyval_list
%type <desc_val> value
%type <array_val> array array_content value_list

%%

start: { $<object_val>$ = new json_map; } object
    {
        print_json($2);
        delete_json_map($2);
    }
    ;

object: '{'  { $<object_val>$ = $<object_val>0; } object_content '}'
    {
        $$ = $3;
    }
    ;

object_content: /* empty object */
    {
        $$ = $<object_val>0;
    }
    | { $<object_val>$ = $<object_val>0; } keyval_list
    {
        $$ = $2;
    }
    ;

keyval_list: keyval_list ',' T_STR ':' value 
    { 
        (*$<object_val>0)[*$3] = $5;
	    delete $3;
        $$ = $<object_val>0;
    }
    | T_STR ':' value 
    {
        (*$<object_val>0)[*$1] = $3;
	    delete $1;
        $$ = $<object_val>0;
    }
    ;

value: T_STR
        { 
            descriptor *d = new descriptor(D_STRING);
            d->value = *$1;
            delete $1;
            $$ = d;
        }
    | T_NUM
        { 
            descriptor *d = new descriptor(D_NUMBER);
            d->value = *$1;
            delete $1;
            $$ = d;
        }
    | T_BOOL
        { 
            descriptor *d = new descriptor(D_BOOLEAN);
            d->value = *$1;
            delete $1;
            $$ = d;
        }
    | T_NULL
        { 
            descriptor *d = new descriptor(D_NULL);
            d->value = *$1;
            delete $1;
            $$ = d;
        }
    | { $<array_val>$ = new json_array; } array
        { 
            descriptor *d = new descriptor(D_ARRAY);
            d->array = $2;
            $$ = d;
        }
            
    | { $<object_val>$ = new json_map; } object
        { 
            descriptor *d = new descriptor(D_OBJECT);
            d->object = $2;
            $$ = d;
        }
    ;

array: '[' { $<array_val>$ = $<array_val>0; } array_content ']'
    {
        $$ = $3;
    }
    ;

array_content: /* empty array */
    {
        $$ = $<array_val>0;
    }
    | { $<array_val>$ = $<array_val>0; } value_list
    {
        $$ = $2;
    }
    ;

value_list: value ',' { $<array_val>$ = $<array_val>0; } value_list
    {
        $<array_val>0->push_back($1);
        $$ = $<array_val>0;
    }
    | value
    {
        $<array_val>0->push_back($1);
        $$ = $<array_val>0;
    }
    ;

%%
