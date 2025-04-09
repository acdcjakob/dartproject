# import numpy as np
# import matplotlib.pyplot as plt

# from src.scoring import calc_score_phi
# from src.scoring import calc_score
# from src.scoring import score_avg_integrand
# from src.findBest import score_avg

# def test_calc_score_phi():
#     h_phi = np.linspace(-np.pi,np.pi,1000)

#     score = np.array([calc_score_phi(hi) for hi in h_phi])

#     plt.plot(h_phi*180/np.pi,score,'x')
#     plt.yticks(np.arange(0,21,1))
#     plt.xticks(np.arange(-180,181,20))
#     plt.grid()
#     plt.show()
    
# def test_calc_score(h_x):
#     # h_x = 0
#     h_y = np.linspace(-200,200,1000) # should span from 3 to 20 over bullseye
#     scr = np.array([calc_score(h_x,hi) for hi in h_y])

#     plt.plot(h_y,scr)
#     plt.grid()
#     plt.show()  

# def test_score_avg_integrand():
#     sigma = np.array([5,5])
#     # aim at 180:
#     t_x = 0
#     t_y = 105

#     h_x = 0
#     h_y = np.linspace(70,130,1000)

#     integrand = np.array([score_avg_integrand(h_x,hi,t_x,t_y,sigma) for hi in h_y])

#     y_180 = np.linspace(99,107,1000)
#     int_180 = np.array([score_avg_integrand(h_x,yi,t_x,t_y,sigma) for yi in y_180])
#     plt.plot(h_y,integrand,label=f'standard deviation vertical: {sigma[1]:.2f}')
#     plt.fill_between(y_180,int_180,color='orange',alpha=.5,label='180 area')
#     plt.xlabel('vertical (mm)')
#     plt.ylabel('weighted score')
#     plt.legend()
#     plt.show()

# def test_score_avg_integrandX():
#     sigma = np.array([10,5])
#     # aim at 180:
#     t_x = 0
#     t_y = 105

#     h_x = np.linspace(-30,30,1000)
#     h_y = 106

#     integrand = np.array([score_avg_integrand(hi,h_y,t_x,t_y,sigma) for hi in h_x])

#     # y_180 = np.linspace(99,107,1000)
#     # int_180 = np.array([score_avg_integrand(h_x,yi,t_x,t_y,sigma) for yi in y_180])
#     plt.plot(h_x,integrand,label=f'standard deviation horizontal: {sigma[0]:.2f}')
#     # plt.fill_between(y_180,int_180,color='orange',alpha=.5,label='180 area')
#     plt.xlabel('vertical (mm)')
#     plt.ylabel('weighted score')
#     plt.legend()
#     plt.show()
    
# def test_score_avg_integrand_multiple():
#     sigma = np.array([5,5])
#     # aim at 180:
#     t_x = 0
#     t_y = 166

#     h_x = np.arange(-15,15,5)
#     t_x = h_x
#     h_y = np.linspace(160,180,1000)
#     for i in range(len(h_x)):
#         integrand = np.array([score_avg_integrand(h_x[i],hi,t_x[i],t_y,sigma) for hi in h_y])

#         # y_180 = np.linspace(99,107,1000)
#         # int_180 = np.array([score_avg_integrand(h_x,yi,t_x,t_y,sigma) for yi in y_180])
#         plt.plot(h_y,integrand,label=f'standard deviation vertical: {sigma[1]:.2f}',alpha=(i+1)/(len(h_x)+1))
#     # plt.fill_between(y_180,int_180,color='orange',alpha=.5,label='180 area')
#     plt.xlabel('vertical (mm)')
#     plt.ylabel('weighted score')
#     plt.legend()
#     plt.show()

# def test_score_avg():
#     return score_avg(0,102,[0.1,0.1])

# # print(test_score_avg())
