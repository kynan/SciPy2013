import numpy as np
import matplotlib
matplotlib.use('Agg')
import pylab

fluidity = np.load('fluidity.npy')
fluidity_mpi = np.load('fluidity_mpi.npy')
dolfin = np.load('dolfin.npy')
dolfin_mpi = np.load('dolfin_mpi.npy')
fluidity_pyop2_seq = np.load('fluidity_pyop2_seq.npy')
fluidity_pyop2_openmp = np.load('fluidity_pyop2_openmp.npy')
fluidity_pyop2_mpi = np.load('fluidity_pyop2_mpi.npy')
fluidity_pyop2_cuda = np.load('fluidity_pyop2_cuda.npy')

fluidity_speedup = fluidity / fluidity
fluidity_mpi_speedup = fluidity / fluidity_mpi
dolfin_speedup = fluidity / dolfin
dolfin_mpi_speedup = fluidity / dolfin_mpi
fluidity_pyop2_seq_speedup = fluidity / fluidity_pyop2_seq
fluidity_pyop2_openmp_speedup = fluidity / fluidity_pyop2_openmp
fluidity_pyop2_mpi_speedup = fluidity / fluidity_pyop2_mpi
fluidity_pyop2_cuda_speedup = fluidity / fluidity_pyop2_cuda

fig = pylab.figure('speedup_linear', figsize=(8, 6), dpi=300)
pylab.plot(np.load('elements.npy'), fluidity_speedup, 'grey', lw=1, label='Fluidity (1 core)')
pylab.plot(np.load('elements.npy'), dolfin_speedup, 'k-.*', lw=2, label='DOLFIN (1 core)')
pylab.plot(np.load('elements.npy'), fluidity_pyop2_seq_speedup, 'y-d', lw=2, label='PyOP2 sequential (1 core)')

pylab.ylim([0, 30])
pylab.legend(loc='best', ncol=2, labelspacing=0.1, prop={'size':12})
pylab.xlabel('Number of elements in the mesh')
pylab.ylabel('Relative speedup over Fluidity baseline')
pylab.title('Benchmark of an advection-diffusion problem for 100 time steps')
pylab.grid()
pylab.savefig('speedup_linear_1.svg', orientation='landscape', format='svg', transparent=True)

pylab.plot(np.load('elements.npy'), fluidity_mpi_speedup, 'g--s', lw=2, label='Fluidity MPI (12 cores)')
pylab.plot(np.load('elements.npy'), dolfin_mpi_speedup, 'b-.+', lw=2, label='DOLFIN MPI (12 cores)')
pylab.plot(np.load('elements.npy'), fluidity_pyop2_mpi_speedup, 'r-<', lw=2, label='PyOP2 MPI (12 cores)')
pylab.legend(loc='best', ncol=2, labelspacing=0.1, prop={'size':12})
pylab.savefig('speedup_linear_2.svg', orientation='landscape', format='svg', transparent=True)

#pylab.plot(np.load('elements.npy'), fluidity_pyop2_openmp_speedup, 'c-v', lw=2, label='PyOP2 OpenMP (12 threads)')
pylab.plot(np.load('elements.npy'), fluidity_pyop2_cuda_speedup, 'm-^', lw=2, label='PyOP2 CUDA (1 GPU)')
pylab.legend(loc='best', ncol=2, labelspacing=0.1, prop={'size':12})
pylab.savefig('speedup_linear_3.svg', orientation='landscape', format='svg', transparent=True)
