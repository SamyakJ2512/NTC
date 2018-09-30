function gcd = EuclidAlgoslow (a, b)
  if a >= 0 && b >= 0 && a + b > 0     %checking for valid inputs
    while a > 0 && b > 0               %iterate till one of them becomes 0
        if a >= b                      
            a = a - b;                 %repeatedly subtracting from bigger value
        else
            b = b - a;
        end
    end
    gcd = max_u(a,b);                    %returning the max of the value after loop ends one of them will be 0 other gcd
    return;
  end
  gcd = -1;                            %if invalid inputs return -1 as gcd
  return;
end
   