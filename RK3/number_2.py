xa = int(input())
ya = int(input())
za = int(input())
xb = int(input())
yb = int(input())
zb = int(input())
xc = int(input())
yc = int(input())
zc = int(input())
print(str((yb - ya) * (zc - za) - (zb - za) * (yc - ya)) + ' ' +
      str((zb - za) * (xc - xa) - (xb - xa) * (zc - za)) + ' ' +
      str((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)))
