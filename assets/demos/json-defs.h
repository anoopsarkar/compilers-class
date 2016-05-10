#ifndef _JSON_DEFS
#define _JSON_DEFS

#include <iostream>
#include <tr1/unordered_map>
#include <vector>
#include <string>

using namespace std;

typedef vector<class descriptor* > json_array;
typedef tr1::unordered_map<string, class descriptor* > json_map;
typedef json_map::iterator json_map_iterator;
typedef json_array::iterator json_array_iterator;

enum descriptor_type {
  D_STRING,
  D_NUMBER,
  D_BOOLEAN,
  D_NULL,
  D_ARRAY,
  D_OBJECT
};

class descriptor {
public:
  	descriptor_type type;
  	string value;
  	json_array *array;
  	json_map *object;

  	descriptor(descriptor_type t) { 
   	 	type = t;  
  	}

	~descriptor() {
		switch (type) {
		case D_STRING:
		case D_NUMBER:
		case D_BOOLEAN:
		case D_NULL: break;
		case D_ARRAY:
			{ 
				json_array_iterator i;
				for (i = array->begin(); i != array->end(); ++i) {
					delete *i;
				}
				delete array;
				break;
    		}
		case D_OBJECT: 
			{ 
				json_map_iterator i;
				for (i = object->begin(); i != object->end(); ++i) {
					delete i->second;
				}
				delete object;
				break;
    		}
		default:
			{
				cerr << "Error: unknown type of descriptor" << endl;
				break;
			}
		}

	}

  	string str() {
		string s;
		switch (type) {
		case D_STRING: { s = "STRING:"; s += value; break; }
		case D_NUMBER: { s = "NUMBER:"; s += value; break; }
		case D_BOOLEAN: { s = "BOOLEAN:"; s += value; break; }
		case D_NULL: { s = "NULL:"; s += value; break; }
		case D_ARRAY: 
			{ 
				s = "ARRAY: ["; 
				json_array_iterator i;
				for (i = array->begin(); i != array->end(); ++i) {
					s += (*i)->str() + ", ";
				}
				s += " ]";
				break; 
			}
		case D_OBJECT: 
			{ 
				s = "\nOBJECT:{ ";
				json_map_iterator i;
				for (i = object->begin(); i != object->end(); ++i) {
					s += i->first + ':' + i->second->str() + ", ";
				}
				s += " }\n";
				break;
    		}
		default:
			{
				cerr << "Error: unknown type of descriptor" << endl;
				break;
			}
		}
	return s;
	}
};

extern "C"
{
  int yyerror(const char *);
  int yyparse(void);
  int yylex(void);  
  int yywrap(void);
}

#endif
