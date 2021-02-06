#p = 0.40  # proporção da fase gasosa desejada
#R = 2.0  # raio da bolsa plastica
#L = 2.0  # comprimento do biodigestor

carga_diaria = 0.231 # [m³/dia]
trh = 45.0  # [dia^-1]

import csv

class methods():

    import numpy as np

    p = 0.40 #proporção da fase gasosa desejada
    R = 1.0  #raio da bolsa plastica
    L = 6.645  #comprimento do biodigestor

    carga_diaria = 0.231 #[m³/dia]
    trh = 45.0                 #[dia^-1]

    def bio_vol(self):
        return self.carga_diaria * self.trh


    def perimetro_total_transversal(self, raio_da_bolsa_plastica):
        return 2.0*(self.np.pi)*raio_da_bolsa_plastica


    def porcentagem_do_perimetro_transversal_destinado_ao_arco(self):
        return 0.621*self.p**2.0 - 0.042*self.p + 0.352


    def base_da_fossa(self, porcentagem_do_perimetro_transversal_destinado_ao_arco):
        A = porcentagem_do_perimetro_transversal_destinado_ao_arco
        return (-1/3*A +1/3)*self.perimetro_total_transversal(self.R)


    def largura_maior_da_fossa(self):
        b = self.base_da_fossa(self.p)
        return 1.618*b


    def profundidade_da_fossa(self):
        a = self.largura_maior_da_fossa()
        return 0.951*a


    def area_transversal_da_fossa(self):

        return 0.4755*(self.largura_maior_da_fossa()+self.base_da_fossa(self.p))


    def area_total_da_fossa(self):
        return self.area_transversal_da_fossa()/(1.0-self.p)


    def area_da_campana(self):

        return self.area_total_da_fossa() - self.area_transversal_da_fossa()


    def volume_total_do_biodigestor(self):

        return self.area_total_da_fossa()*self.L


    def volume_total_da_fossa(self):

        return self.area_transversal_da_fossa()*self.L


    def volume_total_do_gas(self):

        return self.area_da_campana()*self.L


#def dimensions():

#    dim = methods()

#    p = 0.40  # proporção da fase gasosa desejada
#    R = 2.0  # raio da bolsa plastica
#    L = 2.0  # comprimento do biodigestor

#    carga_diaria = 0.231  # [m³/dia]
#    trh = 45.0  # [dia^-1]

#    return {'bio_vol' : methods.bio_vol(carga_diaria, trh),

#    'perimetro_total_transversal' : methods.perimetro_total_transversal(R),

#    'porcentagem_do_perimetro_transversal_destinado_ao_arco' : methods.porcentagem_do_perimetro_transversal_destinado_ao_arco(),

#    'base_da_fossa' : methods.base_da_fossa(methods.porcentagem_do_perimetro_transversal_destinado_ao_arco),

#    'largura_maior_da_fossa' : methods.largura_maior_da_fossa(),

#    'profundidade_da_fossa' : methods.profundidade_da_fossa(),

#    'area_transversal_da_fossa' : methods.area_transversal_da_fossa(),
#
#    'area_total_da_fossa' : methods.area_total_da_fossa(),

#    'area_da_campana' : methods.area_da_campana(),

#    'volume_total_do_biodigestor' : methods.volume_total_do_biodigestor(L),

#    'volume_total_da_fossa' : methods.volume_total_da_fossa(L),

#    'volume_total_do_gas' : methods.volume_total_do_gas(L)

#    }


dim = methods()

r1 = [["Largura maior da parte liquida", dim.largura_maior_da_fossa(), "[m]"],
      ["Base da fossa ", dim.base_da_fossa(dim.porcentagem_do_perimetro_transversal_destinado_ao_arco()), "[m]"],
      ["Profundidade da fossa destinada aos dejetos", dim.profundidade_da_fossa(), "[m]"],
      ["Área transversal da fossa destinada aos dejetos", dim.area_transversal_da_fossa()*0.95, "[m²]"],
      ["Área total transversal", dim.area_total_da_fossa(), "[m²]"],
      ["Área da campana ", dim.area_da_campana(), "[m²]"],
      ["Volume total do biodigestor ", dim.volume_total_do_biodigestor(), "[m³]"],
      ["Volume total da fossa ", dim.volume_total_da_fossa(), "[m³]"],
      ["Volume total destinado ao gás ", dim.volume_total_do_gas(), "[m³]"],
      ["Volume útil do biodigestor ", dim.bio_vol(), "[m³]"],
      ["Volume de segurança", dim.volume_total_da_fossa()*0.05, "[m³]"],
      ["Volume do gasômetro", dim.volume_total_do_gas()*0.95, "[m³]"],
      ["Base menor do volume de segurança", dim.largura_maior_da_fossa(), "[m]"],
      ["Base maior do volume de segurança", dim.largura_maior_da_fossa() + 2*0.022, "[m]"],
      ["Altura do volume de segurança", dim.profundidade_da_fossa()*0.05, "[m]"],
      ["Area da geomembrana para a fossa", 39.04312783 + 0.52996833108, "[m²]"],
      ["Area da geomembrana para o gasômetro", 6.708638536-0.52996833108, "[m²]"],
      ["Area total da geomembrana", 45.75176637, "[m²]"]]

arq = open('data.csv','w')
w = csv.writer(arq)

for row in r1:
    w.writerow(row)

arq.close()

#w.writerow("largura maior da fossa: ", dim.largura_maior_da_fossa(), "[m]")
#w.writerow("base da fossa: ", dim.base_da_fossa(dim.porcentagem_do_perimetro_transversal_destinado_ao_arco()), "[m]")
#w.writerow("perimetro total transversal: ", dim.perimetro_total_transversal(2.0), "[m]")
#w.writerow("profundidade da fossa: ", dim.profundidade_da_fossa(), "[m]")
#w.writerow("area transversal da fossa: ", dim.area_transversal_da_fossa(), "[m²]")
#w.writerow("area total da fossa:", dim.area_total_da_fossa(), "[m²]")
#w.writerow("area da campana: ", dim.area_da_campana(), "[m²]")
#w.writerow("volume total do biodigestor: ", dim.volume_total_do_biodigestor(), "[m³]")
#w.writerow("volume total da fossa: ", dim.volume_total_da_fossa(), "[m³]")
#w.writerow("volume total destinado ao gás: ", dim.volume_total_do_gas(), "[m³]")
#w.writerow("volume util do biodigestor: ", dim.bio_vol(), "[m³]")
#data = {'largura maior da fossa': dim.largura_maior_da_fossa(),
#'base da fossa': dim.base_da_fossa(dim.porcentagem_do_perimetro_transversal_destinado_ao_arco()),
#"perimetro total transversal: ", dim.perimetro_total_transversal(2.0),
#"profundidade da fossa: ", dim.profundidade_da_fossa(),
#"area transversal da fossa: ", dim.area_transversal_da_fossa(),
#"area total da fossa:", dim.area_total_da_fossa(),
#"area da campana: ", dim.area_da_campana(),
#volume total da fossa: ", dim.volume_total_da_fossa(),#"volume total destinado ao gás: ", dim.volume_total_do_gas(),
#"volume util do biodigestor: ", dim.bio_vol()}

#print (data)
