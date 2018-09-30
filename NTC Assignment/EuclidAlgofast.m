function gcd = EuclidAlgofast(a, b)
  if a >= 0 && b >= 0 && a + b > 0        %check for valid inputs
      while a > 0 && b > 0                %iterate till one of the value becomes 0
          if a >= b
              a = mod_u(a,b);               %set the bigger value as remainder of the 2 values
          else
              b = mod_u(b,a);
          end
      end
      gcd = max_u(a,b);                    %return max of the 2 values after loop ends, one of them is 0 other gcd
      return;
  end
  gcd = -1;                              %if input not valid return -1
  return
end
  