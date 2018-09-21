function gcd = naivegcd(a, b)
  gcd = -1;
  if (a >= 0) && (b >= 0) && (a + b) > 0
  	if a == 0 || b == 0
        gcd = max(a,b);
        return
    end
  	for d = min(a,b):-1:0
  		if (mod(a,d) == 0) && (mod(b,d) == 0)
            gcd = d;
  			return;
        end
    end
    gcd = 1;
  	return
  end
return;
end




% The following call would take too long
%print(gcd(790933790547, 1849639579327))