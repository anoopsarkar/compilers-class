sub foo { 
  my ($x,$y) = @_; 
  print "foo.x:$x\n"; 
  print "foo.y:$y\n"; 
}

$x = 1;
print "++x, ++x\n";
foo(++$x, ++$x);
print "x:$x\n\n";

$x = 1;
print "x++, x++\n";
foo($x++, $x++);
print "x:$x\n\n";

$x = 1;
print "x++, ++x\n";
foo($x++, ++$x);
print "x:$x\n\n";

$x = 1;
print "++x, x++\n";
foo(++$x, $x++);
print "x:$x\n\n";

