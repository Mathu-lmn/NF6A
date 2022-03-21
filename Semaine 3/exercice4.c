#include <stdio.h>
#include <math.h>


struct CplxCart { float re, im; };
struct CplxPol { float mod, arg; };

struct Cplx { struct CplxCart cart; struct CplxPol pol; };


struct Cplx cartToPol(struct Cplx in) {
    struct Cplx out;

    float real = in.cart.re;
    float imag = in.cart.im;

    //Module
    out.pol.mod = sqrt(real*real + imag*imag);

    //Argument
    out.pol.arg = atanf(imag/real);

    return out;
}

struct Cplx polToCart(struct Cplx in) {
    struct Cplx out;

    float mod = in.pol.mod;
    float arg = in.pol.arg;

    //Real
    out.cart.re = mod*cosf(arg);

    //Imaginary
    out.cart.im = mod*sinf(arg);

    return out;
}

struct Cplx SumCplx(struct Cplx a, struct Cplx b) {
    struct Cplx out;
    //Sum
    out.cart.re = a.cart.re + b.cart.re;
    out.cart.im = a.cart.im + b.cart.im;

    return out;
}

struct Cplx SubCplx(struct Cplx a, struct Cplx b) {
    struct Cplx out;

    //Substract
    out.cart.re = a.cart.re - b.cart.re;
    out.cart.im = a.cart.im - b.cart.im;

    return out;
}

struct Cplx MulCplx(struct Cplx a, struct Cplx b) {
    struct Cplx out;

    //Product (a+ib)*(c+id)=(ac-bd)+i(ad+bc)
    out.cart.re = (a.cart.re*b.cart.re) - (a.cart.im*b.cart.im);
    out.cart.im = (a.cart.re*b.cart.im) + (a.cart.im*b.cart.re);


    return out;
}

struct Cplx DivCplx(struct Cplx a, struct Cplx b) {
    struct Cplx out;

    //Divide (a+ib)/(c+id)=(ac+bd)/(c²+d²) + i(-ad+bc)/(c²+d²)
    out.cart.re = (a.cart.re*b.cart.re+a.cart.im*b.cart.im)/(b.cart.re*b.cart.re+b.cart.im*b.cart.im);
    out.cart.im = (-a.cart.re*b.cart.im+a.cart.im*b.cart.re)/(b.cart.re*b.cart.re+b.cart.im*b.cart.im);

    return out;
}

struct Cplx SqrtCplx(struct Cplx a) {
    struct Cplx out;

    //Square root of complex : sqrt((|a|+a)/2) + i * (b/|b|)*sqrt((|a|-a)/2)
    out.cart.re = sqrtf(((sqrt(a.cart.re*a.cart.re+a.cart.im*a.cart.im))+a.cart.re)/2);
    out.cart.im = (a.cart.im/fabs(a.cart.im))*sqrtf(((sqrt(a.cart.re*a.cart.re+a.cart.im*a.cart.im))-a.cart.re)/2);


    return out;
}

void Eq2Cplx(struct Cplx a, struct Cplx b, struct Cplx c) {
    struct Cplx out;
    struct Cplx delta;
    struct Cplx tmp;
    struct Cplx tmp2;

    //If a = 0 -> Degree 1
    if(a.cart.re == 0 && a.cart.im == 0) {
        printf("We want to solve :\n");
        printf("(%g+%gi)*x + (%g+%gi) = 0\n",b.cart.re,b.cart.im,c.cart.re,c.cart.im);
        printf("_______________________\n");

        //Solution is -c/b
        c.cart.re = -c.cart.re;
        c.cart.im = -c.cart.im;
        out = DivCplx(c, b);

        //Print
        printf("First degree equation have one solution :\n");
        printf("x = %g+%gi\n", out.cart.re, out.cart.im);
    }
    //Degree 2
    else {
        printf(" We want to solve :\n");
        printf("(%g+%gi)*(x^2) + (%g+%gi)*x + (%g+%gi) = 0\n",a.cart.re,a.cart.im,b.cart.re,b.cart.im,c.cart.re,c.cart.im);
        printf("_______________________\n");

        // delta^2 = b*b-4*a*c;
        delta = MulCplx(b, b);
        tmp.cart.re = 4;
        tmp.cart.im = 0;
        tmp = MulCplx(tmp, a);
        tmp = MulCplx(tmp, c);
        delta = SubCplx(delta, tmp);
        delta = SqrtCplx(delta);

        //Solutions (-b+delta)/2a ou (-b-delta)/2a
        tmp = b;
        tmp.cart.re = -tmp.cart.re;
        tmp.cart.im = -tmp.cart.im;
        out = SumCplx(tmp, delta); // We have (-b+delta)
        tmp2 = a;
        tmp2.cart.re = 2*tmp2.cart.re;
        tmp2.cart.im = 2*tmp2.cart.im; // We have 2*a
        out = DivCplx(out,tmp2);
        printf("x1=%g+%gi\nor\n",out.cart.re,out.cart.im); // First solution
        out = SubCplx(tmp, delta);// We have (-b-delta)
        out = DivCplx(out,tmp2);
        printf("x2=%g+%gi\n",out.cart.re,out.cart.im); // Second solution
    }
}


int main()
{
    //define the complex numbers in their cartesian form
    struct Cplx cplx1, cplx2, cplx3;

    cplx1.cart.re = 10.1;
    cplx1.cart.im = 3.14;

    cplx2.cart.re = 2;
    cplx2.cart.im = 2;


    cplx3.cart.re = 9;
    cplx3.cart.im = 1;
 
    printf("\nCartesian number : %.3f+%.3fi\n", cplx1.cart.re, cplx1.cart.im);
    
    cplx1 = cartToPol(cplx1);
    printf("Number converted to polar : %.3f*e^(i*%.3f)\n", cplx1.pol.mod, cplx1.pol.arg);
    
    cplx1 = polToCart(cplx1);
    printf("Number converted back to cartesian : %.3f+%.3fi\n\n\n", cplx1.cart.re, cplx1.cart.im);

    //Sum
    printf("(%.3f+%.3fi) + (%.3f+%.3fi) = ", cplx1.cart.re, cplx1.cart.im, cplx3.cart.re, cplx3.cart.im);

    cplx1 = SumCplx(cplx1,cplx3);

    printf("%.3f+%.3fi\n", cplx1.cart.re, cplx1.cart.im);


    //Substract
    printf("(%.3f+%.3fi) - (%.3f+%.3fi) = ", cplx1.cart.re, cplx1.cart.im, cplx2.cart.re, cplx2.cart.im);

    cplx1 = SubCplx(cplx1,cplx2);

    printf("%.3f+i%.3f\n", cplx1.cart.re, cplx1.cart.im);


    //Product
    printf("(%.3f+%.3fi) * (%.3f+%.3fi) = ", cplx1.cart.re, cplx1.cart.im, cplx2.cart.re, cplx2.cart.im);
    
    cplx1 = MulCplx(cplx1,cplx2);

    printf("%.3f+%.3fi\n", cplx1.cart.re, cplx1.cart.im);


    //Division
    printf("(%.3f+%.3fi) / (%.3f+%.3fi) = ", cplx1.cart.re, cplx1.cart.im, cplx2.cart.re, cplx2.cart.im);

    cplx1 = DivCplx(cplx1,cplx2);

    printf("%.3f+%.3fi\n\n", cplx1.cart.re, cplx1.cart.im);


    //Second degree equation
    Eq2Cplx(cplx1,cplx2,cplx3);

    return 0;
}