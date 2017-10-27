function area=rsum2(f,a,b,n)
%RSUM2: Computes a Riemann Sum for the function f on
%the interval [a,b] with a regular partition of n points.
%The points on the intervals are chosen as midpoints.


% If the interval ranges from a to b and is partitioned 
% into n points, then the width of each partition is dx.
dx = (b-a)/n;

% Creates a vector of endpoints starting at the midpoint of 
% the first partition and ending at the midpoint of the last partition.
x = a+dx/2:dx:b-dx/2;

% Evaluates the function at each of the values stored in vector x.
y= f(x);

% Computes the area by multiplying the heights in x by the
% partition width dx and adding up over every piece
area = dx*sum(y);