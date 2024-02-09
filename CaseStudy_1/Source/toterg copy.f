      SUBROUTINE TOTERG(Ener, Vir, Lambda, derEn)
c
c     calculates total energy
c
c  Ener (output) : total energy
c  Vir  (output) : total virial
c

      IMPLICIT NONE
      INCLUDE 'parameter.inc'
      INCLUDE 'conf.inc'
      INCLUDE 'potential.inc'
      INCLUDE 'system.inc'

      DOUBLE PRECISION sig3, ri3, CORD
      DOUBLE PRECISION ri9d9, ri3d3, term1, term2
      DOUBLE PRECISION xi, yi, zi, Ener, eni, CORU, viri, Vir, rho
      DOUBLE PRECISION Lambda, derEn, derEni
      INTEGER i, jb
      CHARACTER(LEN=50) :: filename
      LOGICAL :: file_exists
      INTEGER :: unit_number

c     ----- tail correction for derEn
      sig3 = SIG2*SQRT(SIG2)
      ri3 = sig3/(RC*RC*RC)
      ri3d3 = ri3 / 3
      ri9d9 = (ri3 * ri3 * ri3) / 9

      term1 = 5*Lambda**4 / 9.0 * (ri9d9 - ri3d3)
      term2 = 3*Lambda**2 / 3.0 * ri3d3

      CORD = 2 * PI * EPS4 * rho * sig3 * (term1 - term2)


      
      Ener = 0
      Vir = 0
      derEn = 0
      
      ! Open file and check if it exists
      filename = 'derEn.txt'
      INQUIRE(file=filename, exist=file_exists)

      IF (.NOT. file_exists) THEN
            ! Create the file if it doesn't exist
            OPEN(NEWUNIT=unit_number, FILE=filename, STATUS='NEW')
            CLOSE(unit_number)
      END IF

      ! Open the file for appending data
      OPEN(NEWUNIT=unit_number, FILE=filename, STATUS='APPEND', ACTION='WRITE')

      DO i = 1, NPART - 1
            xi = X(i)
            yi = Y(i)
            zi = Z(i)
            jb = i + 1
            CALL ENERI(xi, yi, zi, i, jb, eni, viri, Lambda, derEni)
            Ener = Ener + eni
            Vir = Vir + viri
            derEn = derEn + derEni
      END DO

      ! Write derEn to the file
      WRITE(unit_number, '(F12.6)') derEn

      ! Close the file
      CLOSE(unit_number)

c     ---add tail corrections
      IF (TAILCO) THEN
            rho = NPART/(BOX**3)
            Ener = Ener + NPART*CORU(RC, rho, Lambda)
c         derEn = derEn + NPART*CORD
      END IF
      RETURN
      END
