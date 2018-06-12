# -*- coding: utf-8 -*-

from openerp.osv import fields, osv, orm
# appel des elements de la societe dans cnp


# declaration de la classe cnps dans fiscalité
class declaration_cnps(osv.osv): 
    _name = 'declaration.cnps'
    _columns = {
         # les champs se trouvant hors des tableaux
        'sequencecnps': fields.char('Sequence'),
        'datecnps': fields.date('Date'),
        'periodicitecnps':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité'),
        'impositioncnps_id':fields.char("Période d'imposition"),
        'namecnps_ids':fields.char('Raison Sociale'),
        'bpcnps_id':fields.char('Adresse'),
        'telcnps_id':fields.char('Tel'),
        'servicecnps':fields.char("Service d'assiete des impot"),
        'ncccnps_ids':fields.char("NCC"),
        'codeetablcnps_id':fields.char('Code Etabl'),
        'codeactivcnps_id':fields.char('Code Acctiv'),
        'employeur':fields.float("N° Employeur"),
        # saisie des champs du 1er tableau de la declaration CNPS:
        'mois': fields.selection([('janvier','Janvier'),('fevrier','Février'),('mars','Mars'), ('avril','Avril'),('mai','Mai'),('juin','Juin'),('juillet','Juillet'),('aout','Aoùt'),('septembre','Septembre'), ('octobre','Octobre'),('novembre','Novembre'),('decembre','Decembre')],'Mois',readonly=False, translate=True),
        'hjoi3231jours1': fields.float(size=25,  translate=True),
        'hjoi3231jours2': fields.float(size=25,  translate=True),
        'hjoi3231jours3': fields.float(size=25,  translate=True),
        'hjos3231jours1': fields.float(size=25,  translate=True),
        'hjos3231jours2': fields.float(size=25,  translate=True),
        'hjos3231jours3': fields.float(size=25,  translate=True),
        'mi70000mois1': fields.float(size=25,  translate=True),
        'mi70000mois2': fields.float(size=25,  translate=True),
        'mi70000mois3': fields.float(size=25,  translate=True),
        'ms70000mois1': fields.float(size=25,  translate=True),
        'ms70000mois2': fields.float(size=25,  translate=True),
        'ms70000mois3': fields.float(size=25,  translate=True),
        'ms1647315mois1':fields.float(size=25, translate=True),
        'ms1647315mois2':fields.float(size=25, translate=True),
        'ms1647315mois3':fields.float(size=25, translate=True),
        'csbsactrr':fields.float("Cumul salaires bruts soumis à cotisation au titre du Regime de Retraite.",size=25 ,translate=True, required=True),
        'csbsctrpf':fields.float("Cumul salaires bruts soumis à cotisations au titre des Regimes de Prest Famil. et des Accid. du Travail",size=25 ,translate=True, required=True),
        
        # saisie des champs du 2e tableau de la declaration CNPS:
        'pcprr1':fields.float(size=25, translate=True),
        'pcprr2':fields.float(size=25, translate=True),
        'ppqecp1':fields.float(size=25, translate=True),
        'ppqecp2':fields.float(size=25, translate=True),



        # saisie des champs du 3e tableau de la declaration CNPS:
        'pf1':fields.float(size=25, translate=True),
        'pf2':fields.float(size=25, translate=True),
        'pf3':fields.float("Cotisation due Prestations Familiales",size=25, translate=True),
        'at1':fields.float(size=25, translate=True),
        'at2':fields.float(size=25, translate=True),
        'at3':fields.float("Cotisation due Accidents du Travail",size=25, translate=True),
        'rr1':fields.float(size=25, translate=True),
        'rr2':fields.float(size=25, translate=True),
        'rr3':fields.float("Cotisation due Régime de Retraite",size=25, translate=True),
        'tcap':fields.float("TOTAL COTISATIONS A PAYER",size=25 ,translate=True, required=True),
        
    }
declaration_cnps() # appel de la classe  cnps

# declaration de la classe fdfp dans fiscalité
class declaration_fdfp(osv.osv): 
    _name = 'declaration.fdfp'
    _columns = {
        'sequencefdfp': fields.char('Sequence'),
        'datefdfp': fields.date('Date'),
        'periodicitefdfp':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité'),
        'impositionfdfp_id':fields.char("Période d'imposition"),
        'servicefdfp':fields.char("Service d'assiete des impot"),
        'nccfdfp_ids':fields.char('NCC'),
        # Effectif des salaires
        'effectifdessalairesfdfp':fields.float("01-Effectifs des salaires"),
        # Determination de la taxe
        'remunerationbttafdfp':fields.float(),
        'tauxtafdfp':fields.char(),
        'montantmensueltafdfp':fields.float("MONTANT MENSUEL TA"),
        'remunerationbttfcfp':fields.float(),
        'tauxtfcfdfp':fields.char(),
        'montantmensueltfcfdfp':fields.float("MONTANT MENSUEL (TFC)"),
        'montantcumuletfcfdfp':fields.float("2.3- Montant cumulé de la TFC conservée depuis le début de l’année(3)"),
        'statutregulationfdfp':fields.char("Prise en compte régularisation ?"),
        #regularisation annuelle
        'massesalarialeafdfp':fields.float("3.1 – Masse salariale annuelle"),
        'montanttfcfdfp':fields.float("3.2 – Montant annuel de la TFC (3.1 x 1,2 %)"),
        'montantttfcpayer':fields.float("3.3 - Montant total de la TFC payée au cours de l’année (2.3)"),
        'montanttaxefcfdfp':fields.float("Montant total de la taxe à la formation continue"),
        'engagementpfdfp':fields.float("3.4 - Engagement sur plans agréés par le FDFP (utilisation directe)"),
        'versementaeffcfdfp':fields.float("3.5- Versement à effectuer si |3.2| est supérieur à |3.3| + |3.4|"),
        'montantapayerfdfp':fields.float("MONTANT TOTAL A PAYER (FDFP)"),
        
    }
declaration_fdfp() # appel de la classe  fdfp

# declaration de la classe its  dans fiscalité
class declaration_its(osv.osv): 
    _name = 'declaration.its'
    _columns = {
        'sequenceits': fields.char('Sequence'),
        'dateits': fields.date('Date'),
        'periodiciteits':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité'),
        'impositionits_id':fields.char("Periode d'imposition"),
        'serviceits':fields.char("Service d'assiete des impot"),
        'nccits_id':fields.char('NCC'),
        'sigleits_id':fields.char('Sigle'),
        'objetits_id':fields.char('Objet ou Activité'),
        'adresseits_id': fields.char('Adresse: Commune'),
        'bpits_id':fields.char("Periode d'imposition"),
        'contactits_id':fields.char("Tel"),
        'quartierits_id':fields.char("Quartier"),
        'rueits_id':fields.char("Rue"),
        'mailits_id':fields.char('Adresse electronique'),
        
    }
declaration_its() # appel de la classe  tse
# declaration de la classe tse  dans fiscalité
class declaration_tse(osv.osv): 
    _name = 'declaration.tse'
    _columns = {
        'sequencetse': fields.char('Sequence'),
        'datetse': fields.date('Date'),
        'periodicitetse':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité'),
        'impositiontse_id':fields.char("Periode d'imposition"),
        'servicetse':fields.char("Service d'assiete des impot"),
        'ncctse_id':fields.char('NCC'),
        'chiffreathttse_id':fields.char("CHIFFRE D'AFFAIRE TOTAL HT"),
        'operationexadtse':fields.float("Operations exonérées(Produits petroliers) à dediure"),
        'livraisontse_id': fields.char('Livraison à soi-même taxable à dediure'),
        'chiffreaftaxtse':fields.float("chiffre d' affaires taxables"),
        'tauxtse':fields.char('Taux'),
        'montanttaxetse':fields.float('Montant de la taxe'),
        'regulationtse':fields.float('Regulation'),
        'montantapayetse':fields.float('Montant de la taxe à payer'),
        'montantareportertse':fields.float('Montant à reporter'),
        
    }
declaration_tse() # appel de la classe  tse

# declaration de la classe tva dans fiscalité
class declaration_tva(osv.osv): 
    _name = 'declaration.tva'
    _columns = {
        'sequencetva': fields.char('Sequence'),
        'datetva': fields.date('Date'),
        'periodicitetva':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité'),
        'impositiontva_id':fields.char('Raison Social'),
        'servicetva':fields.char("Service d'assiete des impot"),
        'ncctva_id':fields.char('NCC'),
        # opeérations réalisees
        'chiffreathttva':fields.char("Chiffre d' affaire totale HT"),
        'exportationadtva':fields.float("Exportation à deduire"),
        'operationexletva':fields.float("Opérations exonérées légales à deduire"),
        'operationexconvtva':fields.float("Operations exonérées conventionnelles (joindre attestations) à deduire"),
        'autreopetva':fields.float("Autres opérations non taxables à deduire"),
        'differencetva':fields.float("Différence"),
        'livraisontva': fields.char('Livraison à soi-même taxable à dediure'),
        'chiffreataxhttva':fields.float("Chiffre d'affaire taxable HT"),
        'chiffreataxhttvabrutea':fields.float("Chiffre d'affaire taxable HT"),
        # tva brute
        'tauxtvabrutea':fields.char("Taux"),
        "montannttvabrutea":fields.float("Montant"),
        'chiffreataxhttvabrutea':fields.float("Chiffre d'affaire taxable HT"),
        'tauxtvabrutea':fields.char("Taux"),
        "montannttvabrutea":fields.float("Montant"),
        'chiffreataxhttvabruteb':fields.float("Chiffre d'affaire taxable HT"),
        'tauxtvabruteb':fields.char("Taux"),
        "montannttvabruteb":fields.float("Montant"),
        # regularisation tva 
        'anterieuradeduitereserve':fields.float(" ANTERIEUREMENT DEDUITE A REVERSER"),
        'etatdestaxesduductibledumoi':fields.float('Taxes déductibles du mois'),
        'creditdumoisprecedant':fields.float(" Crédit reporté du mois précédent"),
        'etatsdestaxesdeductibles':fields.char("Etat des taxes deductibles"),
        'totaldeduction':fields.float("TOTAL DEDUCTION"),
        # TOTAL BRUTE
        'totaltvabrute':fields.float("4 - TOTAL TVA BRUTE"),
        'tvanetapayer':fields.float("TVA nette à payer"),
        'creditareporter':fields.float("Crédit à reporter"),
        'creditdemandearembourse':fields.float("Crédit demandé en remboursement"),
        
    }
declaration_tva() # appel de la classe  tva  

# declaration de la classe etats des taxes deductibles dans fiscalité
class declaration_etat(osv.osv): 
    _name = 'declaration.etat'
    _columns = {
        'sequenceetat': fields.char('Sequence'),
        'dateetat': fields.date('Date'),
        'periodiciteetat':fields.selection([('semestre','Semestre'),('trimestre','Trimestre'),('annuelle','Annuelle')],'Periodicité'),
        'impositionetat_id':fields.char("Periode d'imposition"),
        'serviceetat':fields.char("Service d'assiete des impot"),
        'nccetat_id':fields.char( 'NCC'),
        'totaletat':fields.float('Total'),

        # ajout des elements d'etat
        'datefactetat':fields.date("Date de la facture ou de l'importation",),
        'fournisseurnpetat':fields.char("FOURNISSEUR NOM ET PRENOMS"),
        'fournisseurnccetat':fields.char("Fournisseur N° C. C."),
        'referencefactetat':fields.char("REFERENCE DE LA FACTURE OU N° DE LA DECLARATION ET DE LA LIQUIDATION EN DOUANE"),
        'naturebienetat':fields.char("NATURE DES BIENS OU SERVICES (ouvrant droit à déduction)"),
        'montantttetat':fields.float("MONTANT TOTAL"),
        'montanttaxetat':fields.float("MONTANT DE LA TAXE"),
        'prorataetat':fields.char("PRORATA DE DEDUCTION"),
        'montanttdetat':fields.float("MONTANT DE LA TAXE DEDUCTIBLE"), 
    }
declaration_etat() # appel de la classe  etat des taxes deductible


