# -*- coding: utf-8 -*-

from openerp.osv import fields, osv, orm

# declaration de la classe contribuable dans fiscalité
class declaration_contribuable(osv.osv):
    _name = 'declaration.contribuable'
    _columns = {
        'name_ids': fields.one2many('declaration.cnps','namecnps_id','Non',size=25),
        'sigle_ids': fields.one2many('declaration.its','sigleits_id','Sigle',size=25),
        'mail_ids': fields.one2many('declaration.its','mailits_id','Email',size=25),
        'adresse_ids': fields.one2many('declaration.its','adresseits_id','Adresse: Commune',size=25),
        'objet_ids': fields.one2many('declaration.its','objetits_id','Objet ou Activité',size=25),
        'contact_ids': fields.one2many('declaration.its','contactits_id','Tel',size=25),
        'imposition_ids': fields.many2many('declaration.its','impositionits_id','declaration.tva','impositiontva_id',"Periode d'imposition",size=25),
        'codeetabl_ids': fields.one2many('declaration.cnps','codeetablcnps_ids',"Code Etabl",size=25),
        'bp_ids':fields.one2many('declaration.its','bpits_id','BP',size=25),
        'rue_ids':fields.one2many('declaration.its','rueits_id','declaration.tva','bptva_id',"BP",size=25),
        'quartier_ids':fields.one2many('declaration.its','quartierits_id',"Quartier",size=25),
        'ncc_ids':fields.many2many('declaration.its', 'nccits_id', 'declaration.tva', 'ncctva_id','declaration.etat','nccetat_id'),
        
    }
declaration_contribuable() # appel de la classe contribuable

# declaration de la classe cnps dans fiscalité
class declaration_cnps(osv.osv): 
    _name = 'declaration.cnps'
    _columns = {
        'sequencecnps': fields.char('Sequence',size=25, required=True),
        'datecnps': fields.date('Date',size=25, required=True),
        'periodicitecnps':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité', size=25, required=True),
        'servicecnps':fields.char("Service d'assiete des impot",size=25, required=True),
        'namecnps_ids':fields.many2many('declaration.contribuable','Raison Sociale',ondelete='cascade',size=25, required=True),
        'codeetablcnps_ids':fields.many2one('declaration.contribuable','NCC',ondelete='cascade',size=25, required=True),
        
    }
declaration_cnps() # appel de la classe  cnps

# declaration de la classe fdfp dans fiscalité
class declaration_fdfp(osv.osv): 
    _name = 'declaration.fdfp'
    _columns = {
        'sequencefdfp': fields.char('Sequence',size=25, required=True),
        'datefdfp': fields.date('Date',size=25, required=True),
        'periodicitefdfp':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité', size=25, required=True),
        'impositionfdfp_id':fields.many2many('declaration.contribuable',"Période d'imposition",ondelete='cascade',size=25, required=True),
        'servicefdfp':fields.char("Service d'assiete des impot",size=25, required=True),
        'nccfdfp_ids':fields.many2many('declaration.contribuable','NCC',ondelete='cascade',size=25, required=True),
        # Effectif des salaires
        'effectifdessalairesfdfp':fields.float("01-Effectifs des salaires",size=25,required=True),
        # Determination de la taxe
        'remunerationbttafdfp':fields.float(size=25,required=True),
        'tauxtafdfp':fields.char(size=25,required=True),
        'montantmensueltafdfp':fields.float("MONTANT MENSUEL TA",size=25,required=True),
        'remunerationbttfcfp':fields.float(size=25,required=True),
        'tauxtfcfdfp':fields.char(size=25,required=True),
        'montantmensueltfcfdfp':fields.float("MONTANT MENSUEL (TFC)",size=25,required=True),
        'montantcumuletfcfdfp':fields.float("2.3- Montant cumulé de la TFC conservée depuis le début de l’année(3)",size=25),
        'statutregulationfdfp':fields.char("Prise en compte régularisation ?",size=25,required=True),
        #regularisation annuelle
        'massesalarialeafdfp':fields.float("3.1 – Masse salariale annuelle",size=25),
        'montanttfcfdfp':fields.float("3.2 – Montant annuel de la TFC (3.1 x 1,2 %)",size=25),
        'montantttfcpayer':fields.float("3.3 - Montant total de la TFC payée au cours de l’année (2.3)",size=25),
        'montanttaxefcfdfp':fields.floa("Montant total de la taxe à la formation continue",size=25),
        'engagementpfdfp':fields.float("3.4 - Engagement sur plans agréés par le FDFP (utilisation directe)",size=25),
        'versementaeffcfdfp':fields.float("3.5- Versement à effectuer si |3.2| est supérieur à |3.3| + |3.4|",size=25),
        'montantapayerfdfp':fields.float("MONTANT TOTAL A PAYER (FDFP)",size=25),
        
    }
declaration_fdfp() # appel de la classe  fdfp

# declaration de la classe its  dans fiscalité
class declaration_its(osv.osv): 
    _name = 'declaration.its'
    _columns = {
        'sequenceits': fields.char('Sequence',size=25, required=True),
        'dateits': fields.date('Date',size=25, required=True),
        'periodiciteits':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité', size=25, required=True),
        'impositionits_id':fields.many2many('declaration.contribuable',"Periode d'imposition","declaration.fdfp","impositionfdfp_id"),
        'serviceits':fields.char("Service d'assiete des impot",size=25, required=True),
        'nccits_id':fields.many2one('declaration.contribuable','NCC',ondelete='cascade',size=25, required=True),
        'sigleits_id':fields.many2one('declaration.contribuable','Sigle',ondelete='cascade'),
        'objetits_id':fields.many2one('declaration.contribuable','Objet ou Activité',size=25, required=True,ondelete='cascade'),
        'adresseits_id': fields.many2one('declaration.contribuable','Adresse: Commune', ondelete='cascade',size=25, required=True),
        'bpits_id':fields.many2one('declaration.contribuable',"Periode d'imposition",ondelete='cascade'),
        'contactits_id':fields.many2one('declaration.contribuable',"Tel",ondelete='cascade'),
        'quartierits_id':fields.many2one('declaration.contribuable',"Quartier",ondelete='cascade'),
        'rueits_id':fields.many2one('declaration.contribuable',"Rue",ondelete='cascade'),
        'mailits_id':fields.many2one('declaration.contribuable','Adresse electronique',ondelete='cascade'),
        
    }
declaration_its() # appel de la classe  tse
# declaration de la classe tse  dans fiscalité
class declaration_tse(osv.osv): 
    _name = 'declaration.tse'
    _columns = {
        'sequencetse': fields.char('Sequence',size=25, required=True),
        'datetse': fields.date('Date',size=25, required=True),
        'periodicitetse':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité', size=25, required=True),
        'impositiontse_id':fields.many2one('declaration.contribuable',"Periode d'imposition",ondelete='cascade'),
        'servicetse':fields.char("Service d'assiete des impot",size=25, required=True),
        'ncctse_id':fields.many2one('declaration.contribuable','NCC',ondelete='cascade',size=25, required=True),
        'chiffreathttse_id':fields.many2one('declaration.tva',"CHIFFRE D4 AFFAIRE TOTAL HT",ondelete='cascade'),
        'operationexadtse':fields.float("Operations exonérées(Produits petroliers) à dediure",size=25, required=True,ondelete='cascade'),
        'livraisontse_id': fields.many2one('declaration.tva','Livraison à soi-même taxable à dediure',size='cascade'),
        'chiffreaftaxtse':fields.float("chiffre d' affaires taxables",size=25),
        'tauxtse':fields.char('Taux',size=25),
        'montanttaxetse':fields.float('Montant de la taxe',size=25),
        'regulationtse':fields.float('Regulation',size=25),
        'montantapayetse':fields.float('Montant de la taxe à payer',size=25),
        'montantareportertse':fields.float('Montant à reporter',size=25),
        
    }
declaration_tse() # appel de la classe  tse

# declaration de la classe tva dans fiscalité
class declaration_tva(osv.osv): 
    _name = 'declaration.tva'
    _columns = {
        'sequencetva': fields.char('Sequence',size=25, required=True),
        'datetva': fields.date('Date',size=25, required=True),
        'periodicitetva':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité', size=25, required=True),
        'impositiontva_id':fields.many2one('declaration.contribuable','Raison Social',ondelete='cascade', size=25, required=True),
        'servicetva':fields.char("Service d'assiete des impot",size=25, required=True),
        'ncctva_id':fields.many2one('declaration.contribuable','NCC',ondelete='cascade',size=25, required=True),
        # opeérations réalisees
        'chiffreathttva_ids':fields.one2many('declaration.tse','chiffreathttse_id',"Chiffre d' affaire totale HT",size=25),
        'exportationadtva':fields.float("Exportation à deduire",size=25),
        'operationexletva':fields.float("Opérations exonérées légales à deduire",size=25),
        'operationexconvtva':fields.float("Operations exonérées conventionnelles (joindre attestations) à deduire",size=25),
        'autreopetva':fields.float("Autres opérations non taxables à deduire",size=25),
        'differencetva':fields.float("Différence",size=25),
        'livraisontva_ids': fields.one2many('declaration.tse','livraisontse_id','Livraison à soi-même taxable à dediure',size='cascade'),
        'chiffreataxhttva':fields.float("Chiffre d'affaire taxable HT",size=25),
        'chiffreataxhttvabrutea':fields.float("Chiffre d'affaire taxable HT",size=25),
        # tva brute
        'tauxtvabrutea':fields.char("Taux",size=25),
        "montannttvabrutea":fields.float("Montant",size=25),
        'chiffreataxhttvabrutea':fields.float("Chiffre d'affaire taxable HT",size=25),
        'tauxtvabrutea':fields.char("Taux",size=25),
        "montannttvabrutea":fields.float("Montant",size=25),
        'chiffreataxhttvabruteb':fields.float("Chiffre d'affaire taxable HT",size=25),
        'tauxtvabruteb':fields.char("Taux",size=25),
        "montannttvabruteb":fields.float("Montant",size=25),
        # regularisation tva 
        'anterieuradeduitereserve':fields.float(" ANTERIEUREMENT DEDUITE A REVERSER",size=25),
        'etatdestaxesduductibledumoi':fields.float('Taxes déductibles du mois',size=25),
        'creditdumoisprecedant':fields.float(" Crédit reporté du mois précédent",size=25),
        'etatsdestaxesdeductibles':fields.char("Etat des taxes deductibles",size=25),
        'totaldeduction':fields.float("TOTAL DEDUCTION",size=25),
        # TOTAL BRUTE
        'totaltvabrute':fields.float("4 - TOTAL TVA BRUTE",size=25),
        'tvanetapayer':fields.float("TVA nette à payer",size=25),
        'creditareporter':fields.float("Crédit à reporter",size=25),
        'creditdemandearembourse':fields.float("Crédit demandé en remboursement",size=25),
        
    }
declaration_tva() # appel de la classe  tva  

# declaration de la classe etats des taxes deductibles dans fiscalité
class declaration_etat(osv.osv): 
    _name = 'declaration.etat'
    _columns = {
        'sequenceetat': fields.char('Sequence',size=25, required=True),
        'dateetat': fields.date('Date',size=25, required=True),
        'periodiciteetat':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité', size=25, required=True),
        'impositionetat_id':fields.many2one('declaration.contribuable',"Periode d'imposition",ondelete='cascade'),
        'serviceetat':fields.char("Service d'assiete des impot",size=25, required=True),
        'nccetat_id':fields.many2many('declaration.contribuable', 'NCC',ondelete='cascade',size=25, required=True),
        'totaletat':fields.float('Total', size=25,required=True),

        # ajout des elements d'etat
        'datefactetat':fields.date("Date de la facture ou de l'importation",required=True),
        'fournisseurnpetat':fields.char("FOURNISSEUR NOM ET PRENOMS",required=True),
        'fournisseurnccetat':fields.char("Fournisseur N° C. C."),
        'referencefactetat':fields.char("REFERENCE DE LA FACTURE OU N° DE LA DECLARATION ET DE LA LIQUIDATION EN DOUANE"),
        'naturebienetat':fields.char("NATURE DES BIENS OU SERVICES (ouvrant droit à déduction)",required=True),
        'montantttetat':fields.float("MONTANT TOTAL",required=True),
        'montanttaxetat':fields.float("MONTANT DE LA TAXE",required=True),
        'prorataetat':fields.char("PRORATA DE DEDUCTION"),
        'montanttdetat':fields.float("MONTANT DE LA TAXE DEDUCTIBLE", riequired=True), 
    }
declaration_etat() # appel de la classe  etat des taxes deductible


