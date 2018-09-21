function[gcd,x,y] = extended_gcd(a, b)
  if a >= b && b >= 0 && a + b > 0

  if b == 0
      gcd = a;
      x = 1;
      y = 0;
  else
    [gcd, p, q] = extended_gcd(b, mod(a,b));
    x = q;
    y = p - q * fix(a/b);
  end

  if mod(a,gcd) == 0 && mod(b,gcd) == 0
      if gcd == a * x + b * y
          return;
      end
  end
  end
end