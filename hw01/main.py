for ii in range(9,0,-1):
for jj in range(9,0,-1):
if jj <= ii:
    print '{0} * {1} = {2}'.format(ii,jj,str((ii*jj)).rjust(2, ' ')) , ' ',
    print('')
