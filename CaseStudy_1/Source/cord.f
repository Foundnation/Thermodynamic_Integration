        FUNCTION CORU(R, Rho, Lambda)
c
c     tail correction for the energy:
c
c  CORU (output) energy tail correction
c  R    (input)  cutoff radius
c  Rho  (input)  density
c

        IMPLICIT NONE
        INCLUDE 'potential.inc'
        DOUBLE PRECISION sig3, ri3, R, CORU, Rho
        DOUBLE PRECISION Lambda, ri9d9, ri3d3, term1, term2

        sig3 = SIG2*SQRT(SIG2)
        ri3 = sig3/(R*R*R)
        ri3d3 = ri3 / 3
        ri9d9 = (ri3 * ri3 * ri3) / 9

        term1 = 5*Lambda**4 / 9.0 * (ri9d9 - ri3d3)
        term2 = 3*Lambda**2 / 3.0 * ri3d3

        CORU = 2 * PI * EPS4 * Rho * sig3 * (term1 - term2)

c      CORU = 2*PI*EPS4*(Rho*sig3)*(ri3*ri3*ri3/9-ri3/3)


        RETURN
        END
