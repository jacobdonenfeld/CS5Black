function area=rsum1(f,a,b,n)
%RSUM1: Computes a Riemann Sum for the function f on
%the interval [a,b] with a regular partition of n points.
%The points on the intervals are chosen as the right endpoints.

% If the interval ranges from a to b and is partitioned 
% into n points, then the width of each partition is dx.
dx = (b-a)/n;

% Creates a vector of endpoints starting to the right of a
% and ending at b.
x = a+dx:dx:b;

% Evaluates the function at each of the values stored in vector x.
y = f(x);

% Computes the area by multiplying the heights in x by the
% partition width dx and adding up over every piece
area = dx*sum(y);

