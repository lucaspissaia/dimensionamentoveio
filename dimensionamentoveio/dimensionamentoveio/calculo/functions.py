import math
import numpy as np

log = np.log


def Language1(Language):
    return Language


def Ressalto1(ressalto):
    if ressalto == 1:
        Ressalto2 = "Arredondamento no ressalto"
    elif ressalto == 2:
        Ressalto2 = "Sulco no ressalto"
    elif ressalto == 3:
        Ressalto2 = "Canal de fundo plano"
    else:
        Ressalto2 = "Assento de chaveta de extremidade fresada"
    return Ressalto2
    inforessalto = Ressalto1(ressalto)


def Acab1(acabamento):
    if acabamento == 2:
        Acab2 = "Retificado"
    elif acabamento == 1:
        Acab2 = "Usinado ou Laminado a frio"
    elif acabamento == 3:
        Acab2 = 'Laminado a quente'
    else:
        Acab2 = 'Forjado'
    return Acab2
    infoacabamento = Acab1(acabamento)


def Carga1(carga):
    if carga == 1:
        Carga2 = "Flexão pura"
    elif carga == 2:
        Carga2 = "Torção pura"
    else:
        Carga2 = "Flexão e torção"
    return Carga2
    infocarga = Carga1(carga)


def Equil1(equilibrio):
    if equilibrio == 'y':
        Equil2 = "Em equilíbrio"
    else:
        Equil2 = "Em não-equilíbrio"
    return Equil2
    infoequil = Equil1(equilibrio)

def Ressalto1en(ressalto):
    if ressalto == 1:
        Ressalto2 = "Shoulder fillet"
    elif ressalto == 2:
        Ressalto2 = "Grooved round bar"
    elif ressalto == 3:
        Ressalto2 = "Flat-bottom groove"
    else:
        Ressalto2 = "End-mill keyseat r/d = 0.02"
    return Ressalto2
    inforessalto = Ressalto1en(ressalto)


def Acab1en(acabamento):
    if acabamento == 2:
        Acab2 = "Ground"
    elif acabamento == 1:
        Acab2 = "Machined or cold-drawn"
    elif acabamento == 3:
        Acab2 = 'Hot-rolled'
    else:
        Acab2 = 'As-forjed'
    return Acab2
    infoacabamento = Acab1en(acabamento)


def Carga1en(carga):
    if carga == 1:
        Carga2 = "Pure bending"
    elif carga == 2:
        Carga2 = "Pure torsion"
    else:
        Carga2 = "Bending and Torsion"
    return Carga2
    infocarga = Carga1en(carga)


def Equil1en(equilibrio):
    if equilibrio == 'y':
        Equil2 = "In equilibrium"
    else:
        Equil2 = "In non-equilibrium"
    return Equil2
    infoequil = Equil1en(equilibrio)


def Diamvizinha(D):
    return int(D)




def Sut1(TensaoUlt):
    return int(TensaoUlt)

def n1(nseg):
    return float(nseg)

    rr = int(Raioentalhe)
    Sut = Sut1(TensaoUlt)
    acabamento = int(Acab)
    carga = int(Carga)
    temperatura = int(Temp)
    confiabilidade = int(Conf)
    d = int(Diam)
    Sut = int(TensaoUlt)
    eq = str(equilibrio)
    D = int(Dvizinha)
    dinside = int(Dsulco)
    a = int(Larguracanal)
    t2 = int(t)
    Ma = Altmomento
    Mm = int(Mediamomento)
    Tm = int(Mediatorque)
    Ta = int(Alttorque)

    n = n1(nseg)


#####################################################################

# In[115]:
# Third, all figures and also functions for both q and qs are implemented.

def reta(x0, y0, x1, y1, x):
    return (y0 + (y1 - y0) * (x - x0) / (x1 - x0))


def Fig1(rDd, rrd):
    result109 = 0.8299 * (rrd ** (-0.165))
    result12 = 0.8013 * (rrd ** (-0.235))
    result133 = 0.8522 * (rrd ** (-0.232))
    result2 = 0.8148 * (rrd ** (-0.2688))
    if (rDd <= 1.09):
        result = result109
    elif (rDd <= 1.2):
        result = reta(1.09, result109, 1.2, result12, rDd)
    elif (rDd <= 1.33):
        result = reta(1.2, result12, 1.33, result133, rDd)
    elif (rDd <= 2):
        result = result = reta(1.33, result133, 2, result2, rDd)
    else:
        result = result2
    return result


# In[116]:


def Fig2(rDd, rrd):
    result102 = 0.917 * (rrd ** (-0.2039))
    result105 = 0.9223 * (rrd ** (-0.2292))
    result11 = 0.9040 * (rrd ** (-0.2511))
    result15 = 0.8729 * (rrd ** (-0.2922))
    result3 = 0.8936 * (rrd ** (-0.3107))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.1):
        result = reta(1.1, result11, 1.05, result105, rDd)
    elif (rDd <= 1.5):
        result = reta(1.5, result15, 1.1, result11, rDd)
    elif (rDd <= 3):
        result = reta(1.5, result15, 3, result3, rDd)
    else:
        result = result3
    return result


# In[117]:


def Fig3(rDd, rrd):
    result102 = 0.9932 * (rrd ** (-0.2006))
    result105 = 0.9731 * (rrd ** (-0.2593))
    result15 = 0.9579 * (rrd ** (-0.3201))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.5):
        result = reta(1.5, result15, 1.05, result105, rDd)
    else:
        result = result15
    return result


# In[118]:


def Fig4(rDd, rrd):
    result102 = 0.9872 * (rrd ** (-0.1196))
    result105 = 0.9632 * (rrd ** (-0.1587))
    result13 = 0.8667 * (rrd ** (-0.2522))
    if (rDd <= 1.02):
        result = result102
    elif (rDd <= 1.05):
        result = reta(1.02, result102, 1.05, result105, rDd)
    elif (rDd <= 1.3):
        result = reta(1.3, result13, 1.05, result105, rDd)
    else:
        result = result13
    return result


# In[119]:


def Fig5(rrt, rat):
    result003 = -0.8134 * log(rat) + 8.6878
    result004 = -0.7040 * log(rat) + 7.7962
    result005 = -0.6386 * log(rat) + 7.1864
    result007 = -0.5793 * log(rat) + 6.3311
    result010 = -0.4445 * log(rat) + 5.5212
    result015 = -0.4971 * log(rat) + 4.9092
    result020 = -0.4534 * log(rat) + 4.5660
    result040 = -0.5045 * log(rat) + 3.8376
    result060 = -0.6052 * log(rat) + 3.6449
    result1 = -0.7237 * log(rat) + 3.5022
    if rrt <= 0.03:
        result = result003
    elif rrt <= 0.04:
        result = reta(0.03, result003, 0.04, result004, rrt)
    elif rrt <= 0.05:
        result = reta(0.05, result005, 0.04, result004, rrt)
    elif rrt <= 0.07:
        result = reta(0.05, result005, 0.07, result007, rrt)
    elif rrt <= 0.10:
        result = reta(0.10, result010, 0.07, result007, rrt)
    elif rrt <= 0.15:
        result = reta(0.10, result010, 0.15, result015, rrt)
    elif rrt <= 0.2:
        result = reta(0.2, result020, 0.15, result015, rrt)
    elif rrt <= 0.4:
        result = reta(0.2, result020, 0.4, result040, rrt)
    elif rrt <= 0.6:
        result = reta(0.6, result060, 0.4, result040, rrt)
    elif rrt <= 1:
        result = reta(0.6, result060, 1, result1, rrt)
    else:
        result = result1
    return result


# In[120]:


def Fig6(rrt, rat):
    result003 = -0.0871 * log(rat) + 4.6640
    result004 = -0.1608 * log(rat) + 4.2970
    result006 = -0.1608 * log(rat) + 3.7970
    result010 = -0.2552 * log(rat) + 3.2393
    result020 = -0.2244 * log(rat) + 2.6760
    if rrt <= 0.03:
        result = result003
    elif rrt <= 0.04:
        result = reta(0.03, result003, 0.04, result004, rrt)
    elif rrt <= 0.06:
        result = reta(0.06, result006, 0.04, result004, rrt)
    elif rrt <= 0.1:
        result = reta(0.06, result006, 0.1, result010, rrt)
    elif rrt <= 0.2:
        result = reta(0.1, result010, 0.20, result020, rrt)
    else:
        result = result020
    return result


# In[121]:


# In[123]:


def q(Sut, r):
    Neuber = 0.246 - 0.308e-2 * (Sut / 6.89) + 0.151e-4 * (Sut / 6.89) ** 2 - 0.267e-7 * (Sut / 6.89) ** 3
    Neuber *= 25.4 ** 0.5
    return (1 / (1 + Neuber / (r ** 0.5)))


# In[124]:


def qs(Sut, r):
    Neuber = 0.190 - 2.51e-3 * (Sut / 6.89) + 1.35e-5 * (Sut / 6.89) ** 2 - 2.67e-8 * (Sut / 6.89) ** 3
    Neuber *= 25.4 ** 0.5
    return (1 / (1 + Neuber / (r ** 0.5)))


##in1 e in2
def valorin1(ressalto, d, D, rr, dinside, t2):
    if ressalto == 1:
        in1 = D / d
    elif ressalto == 2:
        in1 = d / (d - 2 * dinside)
        D = d
    elif ressalto == 3:
        in1 = rr / t2
    else:
        in1 = 3000
    return in1


def valorin2(ressalto, d, r, dinside, a, t2):
    if ressalto == 1:
        in2 = r / d
    elif ressalto == 2:
        in2 = r / (d - 2 * dinside)
    elif ressalto == 3:
        in2 = a / t2
    else:
        in2 = 3000
    return in2


# In[125]:


def Kt(ressalto, in1, in2):
    if ressalto == 1:
        Kt = Fig2(in1, in2)
    elif ressalto == 2:
        Kt = Fig3(in1, in2)
    elif ressalto == 3:
        Kt = Fig5(in1, in2)
    else:
        Kt = 2.14
    return Kt


def Kts(ressalto, in1, in2):
    if ressalto == 1:
        Kts = Fig1(in1, in2)
    elif ressalto == 2:
        Kts = Fig4(in1, in2)
    elif ressalto == 3:
        Kts = Fig6(in1, in2)
    else:
        Kts = 3
    return Kts


def Kf(Sut, r, ressalto, in1, in2):
    return (1 + q(Sut, r) * (Kt(ressalto, in1, in2) - 1))


def Kfs(Sut, r, ressalto, in1, in2):
    return (1 + qs(Sut, r) * (Kts(ressalto, in1, in2) - 1))

    Kfsresult = Kfs(Sut, r, in1, valorin2)


# In[127]:
# After defining Kf and Kfs, one can calculate all stresses as described in the text.

def σa(Sut, r, ressalto, in1, in2, Ma, d):
    return (32 * Kf(Sut, r, ressalto, in1, in2) * Ma / (np.pi * ((d / 10) ** 3)))


def σm(Sut, r, ressalto, in1, in2, Mm, d):
    return (32 * Kf(Sut, r, ressalto, in1, in2) * Mm / (np.pi * ((d / 10) ** 3)))


def τa(Sut, r, ressalto, in1, in2, Ta, d):
    return (16 * Kfs(Sut, r, ressalto, in1, in2) * Ta / (np.pi * ((d / 10) ** 3)))


def τm(Sut, r, ressalto, in1, in2, Tm, d):
    return (16 * Kfs(Sut, r, ressalto, in1, in2) * Tm / (np.pi * ((d / 10) ** 3)))


# In[128]:


def σal(Sut, r, ressalto, in1, in2, Ma, d, Ta):
    return (σa(Sut, r, ressalto, in1, in2, Ma, d) ** 2 + 3 * τa(Sut, r, ressalto, in1, in2, Ta, d) ** 2) ** 0.5


def σml(Sut, r, ressalto, in1, in2, Mm, d, Tm):
    return (σm(Sut, r, ressalto, in1, in2, Mm, d) ** 2 + 3 * τm(Sut, r, ressalto, in1, in2, Tm, d) ** 2) ** 0.5


def σmax(Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm):
    return ((σm(Sut, r, ressalto, in1, in2, Mm, d) + σa(Sut, r, ressalto, in1, in2, Ma, d)) ** 2 + 3 * (
                τm(Sut, r, ressalto, in1, in2, Tm, d) + τa(Sut, r, ressalto, in1, in2, Ta, d)) ** 2) ** 0.5


# In[129]:
# Next, Se can be calculated

def Sel(Sut):
    if Sut <= 1400:
        Sel = 0.5 * Sut
    else:
        Sel = 700
    return Sel


def ka(Sut, acabamento):
    if acabamento == 1:
        a = 4.51
        b = -0.265
    elif acabamento == 2:
        a = 1.58
        b = -0.085
    elif acabamento == 3:
        a = 57.7
        b = -0.718
    elif acabamento == 4:
        a = 272
        b = -0.995
    return (a * Sut ** b)


def kb(d):
    if d >= 2.79 and d <= 51:
        kb = 1.24 * d ** -0.107
    elif d >= 51 and d <= 254:
        kb = 1.51 * d ** -0.107
    elif d > 254:
        kb = 0.60
    return kb


def kc(carga):
    if carga == 1:
        kc = 1
    elif carga == 2:
        kc = 0.59
    elif carga == 3:
        kc = 1
    return kc


# Definition of kd, avoiding creation of another function.
def kd(temperatura):
    if temperatura == 20:
        kd = 1
    elif temperatura == 50:
        kd = 1.01
    elif temperatura == 100:
        kd = 1.02
    elif temperatura == 150:
        kd = 1.025
    elif temperatura == 200:
        kd = 1.02
    elif temperatura == 250:
        kd = 1
    elif temperatura == 300:
        kd = 0.975
    elif temperatura == 350:
        kd = 0.943
    elif temperatura == 400:
        kd = 0.9
    elif temperatura == 450:
        kd = 0.843
    elif temperatura == 500:
        kd = 0.768
    elif temperatura == 550:
        kd = 0.672
    elif temperatura == 600:
        kd = 0.549
    return kd


def ke(confiabilidade):
    if confiabilidade == 50:
        ke = 1
    elif confiabilidade == 90:
        ke = 0.897
    elif confiabilidade == 95:
        ke = 0.868
    elif confiabilidade == 99:
        ke = 0.814
    elif confiabilidade == 99.9:
        ke = 0.753
    elif confiabilidade == 99.99:
        ke = 0.702
    elif confiabilidade == 99.999:
        ke = 0.659
    elif confiabilidade == 99.9999:
        ke = 0.62
    return ke


kf = 1


def Se(Sut, acabamento, d, carga, temperatura, confiabilidade):
    return Sel(Sut) * ka(Sut, acabamento) * kb(d) * kc(carga) * kd(temperatura) * ke(confiabilidade)


# Resultados dos critérios para fator de segurança e diâmetro

def Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm):
    return (σal(Sut, r, ressalto, in1, in2, Ma, d, Ta) / Se(Sut, acabamento, d, carga, temperatura,
                                                            confiabilidade) + σml(Sut, r, ressalto, in1, in2, Mm, d,
                                                                                  Tm) / Sut) ** -1


def ηvm(Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy):
    return Sy / σmax(Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm)


def Soderberg(Sut, r, ressalto, in1, in2, Ma, d, Ta, Mm, Tm, acabamento, carga, temperatura, confiabilidade, Sy):
    return (σal(Sut, r, ressalto, in1, in2, Ma, d, Ta) / Se(Sut, acabamento, d, carga, temperatura,
                                                            confiabilidade) + σml(Sut, r, ressalto, in1, in2, Mm, d,
                                                                                  Tm) / Sy) ** -1


'''def ASME(d, Kf, Ma, Se, Kfs, Ta, Mm, Tm, Sy, Sut, r, ressalto, in1, in2, acabamento, carga, temperatura,
         confiabilidade):
    return (1 / 1000) * ((16 / (np.pi * d ** 3)) * (4 * (
                Kf(Sut, r, ressalto, in1, in2) * Ma / Se(Sut, acabamento, d, carga, temperatura,confiabilidade)) ** 2 + 3 * (Kfs(Sut, r, ressalto, in1, in2) *
                Ta / Se(Sut,acabamento, d,carga,temperatura,confiabilidade)) ** 2 + 4 * (Kf(Sut, r, ressalto, in1, in2) * Mm / Sy) ** 2 + 3 * (Kfs(Sut, r, ressalto, in1, in2) * Tm / Sy) ** 2) ** (1 / 2)) ** (-1)
'''

def AGerber(Sut, r, ressalto, in1, in2, Ma, Ta):
    return (4 * (Kf(Sut, r, ressalto, in1, in2) * Ma) ** 2 + 3 * (Kfs(Sut, r, ressalto, in1, in2) * Ta) ** 2) ** 0.5


def BGerber(Sut, r, ressalto, in1, in2, Mm, Tm):
    return (4 * (Kf(Sut, r, ressalto, in1, in2) * Mm) ** 2 + 3 * (Kfs(Sut, r, ressalto, in1, in2) * Tm) ** 2) ** 0.5


def Gerber(Sut, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, acabamento, d, carga, temperatura, confiabilidade):
    if AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) == 0:
        return "Devido a ser torção pura para um veio em equilíbrio, não foi possível calcular o coeficiente de Gerber."
    else:
        return (1 / 1000) * ((8 * AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) / (
                    np.pi * Se(Sut, acabamento, d, carga, temperatura, confiabilidade) * d ** 3)) * (1 + (1 + (
                    2 * BGerber(Sut, r, ressalto, in1, in2, Mm, Tm) * Se(Sut, acabamento, d, carga, temperatura,
                                                                         confiabilidade) / (
                                AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) * Sut)) ** 2) ** 0.5)) ** (-1)

def Gerberen(Sut, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, acabamento, d, carga, temperatura, confiabilidade):
    if AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) == 0:
        return "Due to pure torsion for a shaft in equilibrium, it wasn't possible to calculate the Gerber coefficient."
    else:
        return (1 / 1000) * ((8 * AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) / (
                    np.pi * Se(Sut, acabamento, d, carga, temperatura, confiabilidade) * d ** 3)) * (1 + (1 + (
                    2 * BGerber(Sut, r, ressalto, in1, in2, Mm, Tm) * Se(Sut, acabamento, d, carga, temperatura,
                                                                         confiabilidade) / (
                                AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) * Sut)) ** 2) ** 0.5)) ** (-1)

def fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
    if Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm) <= ηvm(
            Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy) > n:
        resposta = Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm)
    elif Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm) > ηvm(
            Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy) > n:
        resposta = Soderberg(Sut, r, ressalto, in1, in2, Ma, d, Ta, Mm, Tm, acabamento, carga, temperatura, confiabilidade, Sy)
    else:
        resposta = n
    return resposta

def fatordeseg(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
    if Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm) <= ηvm(
            Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy) > n:
        resposta = "O fator de segurança de Goodman é indicado. Falha por escoamento no primeiro ciclo de Von Mises foi verificado e Goodman foi aprovado! Verificar as sugestões do programa."
    elif Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm) > ηvm(
            Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy) > n:
        resposta = "O fator de Goodman falhou na checagem de falha por escoamento, Soderberg é indicado! Verificar as sugestões do programa."
    else:
        resposta = "Todos os fatores indicam falha por fadiga do material, de acordo com seu mínimo tolerável. Verificar as sugestões do programa."
    return resposta

def fatordesegen(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
    if Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm) <= ηvm(
            Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy) > n:
        resposta = "Goodman's safety factor is indicated. Failure by yielding was checked using Von Mises and Goodman passed! Check program suggestions."
    elif Goodman(Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm) > ηvm(
            Sut, r, ressalto, in1, in2, Ma, d, Mm, Ta, Tm, Sy) > n:
        resposta = "Soderberg's safety factor is indicated, since Von Mises indicates failure by yielding for Goodman's safety factor! Check program suggestions."
    else:
        resposta = "All the safety factor point to a fatigue failure, according with your tolerable minimum safety factor value. Check program suggestions."
    return resposta

def infofatordeseg(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
    if 1 >= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
        resposta = "O fator de segurança é muito baixo, há o risco de falha por fadiga. Sugere-se as seguintes opções: aumentar o diâmetro, trocar para um material com mais resistência, acabamento com maior dureza superficial."
    elif 1 <= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) < 1.5:
        resposta = "Um fator de segurança entre 1 e 1.5 é indicado para materiais excepcionalmente confiáveis sob condições controladas com cargas e tensões determinadas facilmente. Sugere-se aumentar o fator de segurança, para isso, tem as " \
                   "seguintes opções: aumentar o diâmetro, trocar para um material com mais resistência, acabamento com maior dureza superficial."
    elif 1.5 <= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) <= 2:
        resposta = "Um fator de segurança entre 1.5 e 2 é indicado para materiais bem conhecidos sob condições razoavelmente constantes com cargas e tensões determinadas facilmente. Para maior segurança, sugere-se aumentar o fator de segurança para acima de 2," \
                   " para isso, tem as seguintes opções: aumentar o diâmetro, trocar para um material com mais resistência, acabamento com maior dureza superficial."
    elif 2 <= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) <= 2.5:
        resposta = "Um fator de segurança entre 2 e 2.5 é o indicado para materiais conhecidos e em ambientes comuns com cargas e tensões que podem ser determinadas. É a faixa indicada por este programa para situações em geral."
    elif 2.5 < fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) <= 3:
        resposta = "Um fator de segurança entre 2.5 e 3 é o indicado para materiais não-testados sob condições médias de ambientes, de cargas e tensões. De acordo com a sua situação, ele pode ter um valor menor, essa decisão é do projetista ou do engenheiro responsável." \
                   "Com algumas mudanças, o veio (eixo) pode ter o seu custo de fabricação reduzido, para isso, sugere-se as seguintes opções: diminuir o diâmetro, trocar para um material com menor resistência, acabamento superficial de menor dureza."
    elif 3 < fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
        resposta = "Um fator de segurança maior do que 3 é indicado para materiais não-testados sob condições médias de ambientes, de cargas e tensões. De acordo com a sua situação, ele pode ter um valor menor, essa decisão é sua." \
                   "Com algumas mudanças, o veio (eixo) pode ter o seu custo de fabricação reduzido, para isso, sugere-se as seguintes opções: diminuir o diâmetro, trocar para um material com menor resistência, acabamento superficial de menor dureza."
    else:
        resposta = ".."
    return resposta


def infofatordesegen(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
    if 1 >= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
        resposta = "The safety factor is too low, there is risk of fatigue failure. The following options are suggested: increase the diameter, change to a material with more resistance, treatment with greater surface hardness."
    elif 1 <= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) < 1.5:
        resposta = "A safety factor between 1 and 1.5 is indicated for exceptionally reliable materials under controlled conditions with easily determined loads and stresses. It is suggested to increase the safety factor value," \
                   " the following options are suggested: increase the diameter, change to a material with more resistance, treatment with greater surface hardness."
    elif 1.5 <= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) <= 2:
        resposta = "A safety factor between 1.5 and 2 is indicated for well-know materials under fairly constant conditions with easily determined loads and stresses. For better safety, it is suggested to increase the safety factor value above 2, " \
                   "for this, you have the following suggetions: increase the diameter, change to a material with more resistance, treatment with greater surface hardness. "
    elif 2 <= fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) <= 2.5:
        resposta = "A safety factor between 2 and 2.5 is suitable for known materials and in common environments with loads and stresses that can be determined. It is the range indicated by this program for general situations."
    elif 2.5 < fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy) <= 3:
        resposta = "A safety factor between 2.5 and 3 is suitable for untested materials under average environment, load and stress conditions. According on your situation, it may have a lower value, but that is a decision that the designer or engineer should take it." \
                   "With some changes, the shaft can have its manufacturing cost reduced, for this, the following options are suggested: reduce the diameter, change to a material with less resistance, treatment with lower surface hardness"
    elif 3 < fator(n, Sut, r, ressalto, in1, in2, Ma, d, Ta, acabamento, carga, temperatura, confiabilidade, Mm, Tm, Sy):
        resposta = "A safety factor bigger than 3 is indicated for untested materials under average environment, loads and stresses conditions. According on your situation, it may have a lower value, but that is a decision that the designer or engineer should take it." \
                   "With some changes, the shaft can have its manufacturing cost reduced, for this, the following options are suggested: reduce the diameter, change to a material with less resistance, treatment with lower surface hardness"
    else:
        resposta = ".."
    return resposta


def dGoodman(n, r, ressalto, in1, in2, acabamento, d, carga, temperatura, confiabilidade, Ma, Kfs, Ta, Mm, Tm, Se, Sut):
    return 10 * (((1 / Se(Sut, acabamento, d, carga, temperatura, confiabilidade)) * (
                4 * (Kf(Sut, r, ressalto, in1, in2) * Ma) ** 2 + 3 * (
                    Kfs(Sut, r, ressalto, in1, in2) * Ta) ** 2) ** 0.5 + (1 / Sut) * (
                              4 * (Kf(Sut, r, ressalto, in1, in2) * Mm) ** 2 + 3 * (
                                  Kfs(Sut, r, ressalto, in1, in2) * Tm) ** 2) ** (1 / 2)) * (16 * n / np.pi)) ** (1 / 3)


def dSoderberg(n, Sut, acabamento, d, carga, temperatura, confiabilidade, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, Se,
               Sy):
    return 10 * (((1 / Se(Sut, acabamento, d, carga, temperatura, confiabilidade)) * (
                4 * (Kf(Sut, r, ressalto, in1, in2) * Ma) ** 2 + 3 * (
                    Kfs(Sut, r, ressalto, in1, in2) * Ta) ** 2) ** 0.5 + (1 / Sy) * (
                              4 * (Kf(Sut, r, ressalto, in1, in2) * Mm) ** 2 + 3 * (
                                  Kfs(Sut, r, ressalto, in1, in2) * Tm) ** 2) ** (1 / 2)) * (16 * n / np.pi)) ** (1 / 3)


def dvm(n, Sut, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, Sy):
    return (((1 / ((np.pi * (Sy / n)) ** 2)) * ((32 * Kf(Sut, r, ressalto, in1, in2) * (Mm + Ma)) ** 2 + 3 * (
                16 * Kfs(Sut, r, ressalto, in1, in2) * (Tm + Ta)) ** 2)) ** (1 / 6)) * 10


'''def dASME(n, Sut, r, ressalto, in1, in2, Ma, acabamento, d, carga, temperatura, confiabilidade, Ta, Mm, Tm, Sy):
    return 10 * ((16 * n / np.pi) * (4 * (
                Kf(Sut, r, ressalto, in1, in2) * Ma / Se(Sut, acabamento, d, carga, temperatura,
                                                         confiabilidade)) ** 2 + 3 * (
                                                 Kfs(Sut, r, ressalto, in1, in2) * Ta / Se(Sut, acabamento, d, carga,
                                                                                           temperatura,
                                                                                           confiabilidade)) ** 2 + 4 * (
                                                 Kf(Sut, r, ressalto, in1, in2) * Mm / Sy) ** 2 + 3 * (
                                                 Kfs(Sut, r, ressalto, in1, in2) * Tm / Sy) ** 2) ** 0.5) ** (1 / 3)'''


def dGerber(Sut, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, n, acabamento, d, carga, temperatura, confiabilidade):
    if AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) == 0:
        return 'Devido a ser torção pura para um veio em equilíbrio, não foi possível calcular o diâmetro por Gerber.'
    else:
        return 10 * ((8 * n * AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) / (
                    np.pi * Se(Sut, acabamento, d, carga, temperatura, confiabilidade))) * (1 + (1 + (
                    2 * BGerber(Sut, r, ressalto, in1, in2, Mm, Tm) * Se(Sut, acabamento, d, carga, temperatura,
                                                                         confiabilidade) / (
                                AGerber(Sut, r, ressalto, in1, in2, Ma, Ta) * Sut)) ** 2) ** 0.5)) ** (1 / 3)


def diameter(n, r, ressalto, in1, in2, acabamento, d, carga, temperatura, confiabilidade, Ma, Ta, Mm, Tm, Sy, Sut):
    if dGoodman(n, r, ressalto, in1, in2, acabamento, d, carga, temperatura, confiabilidade, Ma, Kfs, Ta, Mm, Tm, Se,
                Sut) >= dvm(n, Sut, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, Sy):
        d = "O valor sugerido é o diâmetro de Goodman, falha de escoamento foi checada pelo critério de Von Mises e Goodman foi aprovado. Verificar as sugestões do programa."
    else:
        d = "Há risco de falha por escoamento, portanto, o diâmetro sugerido é o pelo critério de Soderberg. Verificar as sugestões do programa."
    return d

def diameteren(n, r, ressalto, in1, in2, acabamento, d, carga, temperatura, confiabilidade, Ma, Ta, Mm, Tm, Sy, Sut):
    if dGoodman(n, r, ressalto, in1, in2, acabamento, d, carga, temperatura, confiabilidade, Ma, Kfs, Ta, Mm, Tm, Se,
                Sut) >= dvm(n, Sut, r, ressalto, in1, in2, Ma, Ta, Mm, Tm, Sy):
        d = "The suggested value is the diameter by Goodman, failure by yielding was checked using Von Mises' criteria and Goodman was approved. Check program suggestions."
    else:
        d = "Soderberg's diameter is suggested, since Von Mises indicates failure by yielding for Goodman's diameter. Check program suggestions."
    return d


def infogeralptd():
    return "Os critérios usados para o cálculo são conhecidos na literatura e indústria, ASME e Gerber são mais recentes e menos conservadores, logo, a análise é feita entre Goodman e Soderberg."
def infogeralend():
    return "The criterias used for the calculus are well know in the literature and industry, ASME and Gerber are more recently and less conservatives, so the analysis is between Goodman and Soderberg."
def infogeralptn():
    return "O valor adotado para o fator de segurança depende da aplicação e da literatura usada, de maneira geral, este programa recomenda valores entre 2 e 2.5. A decisão final é do projetista ou engenheiro responsável."
def infogeralenn():
    return "The value adopted for the safety factor depends on the application and the literature used, for this program the range recomended is between 2 and 2.5. The final decision rests with the responsible designer or engineer."
