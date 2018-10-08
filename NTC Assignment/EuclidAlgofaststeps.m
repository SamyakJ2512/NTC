function gcd = EuclidAlgofaststeps(a, b)
  if a >= 0 && b >= 0 && a + b > 0        %check for valid inputs
      count  = 0;
      while a > 0 && b > 0                %iterate till one of the value becomes 0
          if a >= b
              count = count + 1;
              r = mod_u(a,b);               %set the bigger value as remainder of the 2 values
              q = fix(a/b);
              fprintf('Step %d : %d = %d * %d + %d\n',count,a,b,q,r);
              a=r;
              
          else
              count = count + 1;
              r = mod_u(b,a);
              q = fix(b/a);
              fprintf('Step %d : %d = %d * %d + %d\n',count,b,a,q,r);
              b=r;
          end
      end
      fprintf('Since the remainder is now 0 GCD is %d\n',max_u(a,b));
      gcd = max_u(a,b);                    %return max of the 2 values after loop ends, one of them is 0 other gcd
      return;
  end
  gcd = -1;                              %if input not valid return -1
  return
end
