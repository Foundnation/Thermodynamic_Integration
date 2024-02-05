**==ener.spg  processed by SPAG 4.52O  at 18:54 on 27 Mar 1996
      SUBROUTINE ENER(En, Vir, R2, Lambda, derEn)
c
c     calculate energy
c
c     En : (output) energy
c     Vir: (output) virial
c     R2 : (input) distance squared between two particles
c
      IMPLICIT NONE
      DOUBLE PRECISION R2, r2i, r6i, En, Vir, Lambda, Lambda3, Lambda5
      DOUBLE PRECISION derEn
      INCLUDE 'potential.inc'
 
      IF (R2.LT.RC2) THEN
         r2i = SIG2/R2
         r6i = r2i*r2i*r2i
         Lambda3 = Lambda * Lambda * Lambda
         Lambda5 = Lambda3 * Lambda * Lambda
         IF (SHIFT) THEN
            En = EPS4*(Lambda5*r6i*r6i-Lambda3*r6i) - ECUT
         ELSE
            En = EPS4*(Lambda5*r6i*r6i-Lambda3*r6i)
         END IF
         Vir = EPS48*(Lambda5*r6i*r6i-0.5D0*Lambda3*r6i)
         derEn = EPS4*(5.0d0*Lambda**4*r6i*r6i - 3.0d0*Lambda**2*r6i)
      ELSE
         En = 0
         Vir = 0
      END IF
      RETURN
      END
