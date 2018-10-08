function[gcd,x,y] = extended_gcd(a, b)
  if a >= b && b >= 0 && a + b > 0                     %checking for valid inputs
      if b == 0                                        %if b becomes 0 then a is gcd and gcd=a*x+b*y so x=1 y=0
          gcd = a;
          x = 1;
          y = 0;
      else
          [gcd, p, q] = extended_gcd(b, mod(a,b));     %call recursively the same function with smaller value and remainder of 2 values
          x = q;
          y = p - q * fix_u(a,b);
      end
      if mod_u(a,gcd) == 0 && mod_u(b,gcd) == 0            %if the gcd divides both a and b then terminate recursion 
          if gcd == a * x + b * y
              return;
          end
      end
  end
  gcd = -1;
  return;
end