d = naivegcd(16,24);
fprintf('Naive Gcd %d\n',d);

e = EuclidAlgoslow(16,24);

fprintf('Euclid Algo slow %d\n',e);

e = EuclidAlgofast(16,24);

fprintf('Euclid Algo fast %d\n',e);

[d,x,y] = extended_gcd(100,13);

fprintf('Extended Euclid Algo  %d = 100*%d + 13*%d\n',d,x,y);
