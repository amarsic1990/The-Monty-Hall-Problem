# -*- coding: utf-8 -*-
import numpy as np

def simNagrVrata(brSim):
    """
    simulacija vrata iza kojih se nalazi nagrada. 
    Kao input je potrebno unijeti broj simulacija
    """
    return np.random.randint(0,3, brSim)

def simPog(brSim):
    """
    funkcija vraca odabrana vrata. Npr. mozemo odlucimo se za strategiju da uvijek biramo vrata 0 ili 1 ili 2.
    """
    return np.zeros(brSim, dtype = int)

def pogVrata(nagrVr, pogoVr):
    """
    simulacija pokazivanja vrata iza kojih se ne nalazi nagrada.
    """
    return [np.setdiff1d([0,1,2], [nagrVr[i], pogoVr[i]])[0] for i in range(len(nagrVr))]

def promVr(pogoVr, pogVr):
    """
    strategija mijenjanja inicijalno odabranih vrata nakon što se pokazu vrata koja ne sadrze auto
    """
    return [np.setdiff1d([0,1,2], [pogoVr[i], pogVr[i]])[0] for i in range(len(pogoVr))]

def postPobj(pogoVr, nagrVr):
    """
    funkcija vraca u koliko posto igara osvajamo auto
    """
    return 100 * (pogoVr == nagrVr).mean()

brSim = 10000
print "igru igramo", brSim, "puta"; print; print
tocVrata = simNagrVrata(brSim)
pogoci = simPog(brSim)
krivaVrata = pogVrata(tocVrata, pogoci)
print "kada ne mjenjamo vrata dobivamo u", postPobj(pogoci, tocVrata), "% slucajeva"; print; print
promVrata = promVr(pogoci, krivaVrata)
print "kada  mjenjamo vrata dobivamo u", postPobj(promVrata, tocVrata), "% slucajeva"