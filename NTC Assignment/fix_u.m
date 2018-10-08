function q = fix_u(a,b)
if(a>=b)
    r=mod(a,b);
    q = (a-r)/b;
else
    r=mod(b,a);
    q = (b-r)/a;
end
end
