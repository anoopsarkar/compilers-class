(* string recognition by regexp including intersection
   using Brzozowski's method of derivatives.
   
   written by Neelakantan Krishnaswami <neelk@cs.cmu.edu>

   posted to comp.compilers: 
   http://compilers.iecc.com/comparch/article/07-10-067
*)

(* The datatype of regular expressions. Intersection and union are
      And and Or respectively. *)

type re =
    | Char of char
    | Epsilon
    | Seq of re * re
    | Star of re
    | False
    | Or of re * re
    | True
    | And of re * re

(* Check whether a regular expression matches the empty string. *)

let rec nullable re =
    match re with
    | Char _ -> false
    | Epsilon -> true
    | Seq(r1, r2) -> (nullable r1) && (nullable r2)
    | Star r -> true
    | False -> false
    | Or(r1, r2) -> (nullable r1) || (nullable r2)
    | True -> true
    | And(r1, r2) -> (nullable r1) && (nullable r2)

(* deriv c r computes the c-th "derivative" of r. What this
      means is that we compute a regular expression r' from r, such
      that if (c ^ s) is recognized by r, then r' recognizes s. *)

let rec deriv c re =
    match re with
    | Char c' -> if c = c' then Epsilon else False
    | Epsilon -> False
    | Seq(r1, r2) ->
            let r1' = deriv c r1 in
            if nullable r1 then
Or(Seq(r1', r2), deriv c r2)
            else
Seq(r1', r2)
    | Star r -> Seq(deriv c r, (Star r))
    | False -> False
    | Or(r1, r2) -> Or(deriv c r1, deriv c r2)
    | True -> True
    | And(r1, r2) -> And(deriv c r1, deriv c r2)

(* check uses derivatives to match the substring of s starting at
      position at i. If the i-th character of s is c, then we compute
      the c'th derivative and look at position i+1. *)

let rec check s re i =
    if i = String.length s then
        if nullable re then Some i else None
    else
        check s (deriv s.[i] re) (i+1)


