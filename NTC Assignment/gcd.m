%GCD calculation
%Samyak Jain
%16CO254

prompt = 'Enter the first number : ';         
a = input(prompt);                                %Taking input 1
prompt = 'Enter the second number : ';
b = input(prompt);                                %Taking input 2
t = [0]*4;
d1 = naivegcd(a,b);                               %calling naive gcd function
fprintf('Using Naive Gcd the gcd(%d,%d) is %d\n',a,b,d1);
f1 = @()naivegcd(a,b);
t(1) = timeit(f1);                                %calculation of execution time of naive gcd

d2 = EuclidAlgoslow(a,b);                         %calling slow euclid algo
fprintf('Using slow Euclid Algo the gcd(%d,%d) is %d\n',a,b,d2);
f2 = @()EuclidAlgoslow(a,b);
t(2) = timeit(f2);                                 %calculation of execution time of slow euclid

d3 = EuclidAlgofast(a,b);                          %calling fast Euclid algo
fprintf('Using fast Euclid Algo the gcd(%d,%d) is %d\n',a,b,d3);
f3 = @()EuclidAlgofast(a,b);
t(3) = timeit(f3);                                 %execution time of fast euclid
if(a>b)
    [d4,x,y] = extended_gcd(a,b);                  %extended gcd algo
    fprintf('Using Extended Euclid Algo the gcd(%d,%d) can be expressed as  %d = %d*%d + %d*%d\n',a,b,d4,a,x,b,y);
    f4 = @()extended_gcd(a,b);
    t(4) = timeit(f4);                             %execution time for extended euclid
else
    [d4,x,y] = extended_gcd(b,a);                  %extended gcd algo
    fprintf('Using Extended Euclid Algo the gcd(%d,%d) can be expressed as  %d = %d*%d + %d*%d\n',a,b,d4,b,x,a,y);
    f4 = @()extended_gcd(b,a);
    t(4) = timeit(f4);                              %execution time for extended euclid
end



bar(t);
set(gca,'xticklabel',{'Naive GCD','Euclid fast','Euclid slow','Extended GCD'});
title('Comparison between various GCD calculating Algorithms');
xlabel('Algorithms');
ylabel('Execution Time');
    

