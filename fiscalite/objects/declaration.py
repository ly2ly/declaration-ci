# -*- coding: utf-8 -*-

from openerp.osv import osv, fields, orm


#declaration de la classe contribuable dans fiscalite
class res_company( osv.osv):
    _name = 'res.company'
    _inherit ='res.company'
    _columns =  {
        'sigle':fields.char('Sigle'),
        'objet':fields.char('Objet ou Activité'),
        'service':fields.char("Service d'assiette des impots"),
        'quartier':fields.char("Quartier"),
        'codeetab':fields.char('cde Etab'),
        'codeact':fields.char('cde Activ'),
        'employeur':fields.char('N° Employeur'),
    }

# declaration de la classe elements etats des taxes deductibles dans fiscalité
class declaration_elementetat(osv.osv): 
    _name = 'declaration.elementetat'
    _columns = {

        'element_id':fields.many2one('declaration.etat', 'Order Reference', required=True, ondelete='cascade', domain=[('sale_ok', '=', True)], readonly=True),
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


###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
######################################################               CNPS            ##############################################

# declaration de la classe cnps dans fiscalité
class declaration_cnps(osv.osv): 
    _name = 'declaration.cnps'
    _res_name ='element_id'


    def totalsalaire():
        salaire=hjoi3231jours1+hjos3231jours1+mi70000mois1+ms70000mois1+ms1647315mois1
        return salaire

    def totalregime():
        regime=hjoi3231jours2+hjos3231jours2+mi70000mois2+ms70000mois2+ms1647315mois2
        return regime

    def totaltravail():
        travail=hjoi3231jours3+hjos3231jours3+mi70000mois3+ms70000mois3+ms1647315mois3
        return travail
        
    def calculfamille():
        famille= pf1*pf2
        return famille

    def calcutaccident():
        accident=at1*at2
        return Accidents

    def calculregimes():
        regimes=rr1*rr2
        return regimes
    def totalcotisation():
        total=pf3+at3+rr3
        return total
    def sequencecns():
        sequencecnps=sequencecnps
        return sequencecnps

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
        'hjoi3231jours1': fields.float( ),
        'hjoi3231jours2': fields.float(),
        'hjoi3231jours3': fields.float(),
        'hjos3231jours1': fields.float(),
        'hjos3231jours2': fields.float(),
        'hjos3231jours3': fields.float(),
        'mi70000mois1': fields.float(),
        'mi70000mois2': fields.float(),
        'mi70000mois3': fields.float(),
        'ms70000mois1': fields.float(),
        'ms70000mois2': fields.float(),
        'ms70000mois3': fields.float(),
        'ms1647315mois1':fields.float(),
        'ms1647315mois2':fields.float(),
        'ms1647315mois3':fields.float(),
        'csbsactrr':fields.float("Cumul salaires bruts soumis à cotisation au titre du Regime de Retraite."),
        'csbsctrpf':fields.float("Cumul salaires bruts soumis à cotisations au titre des Regimes de Prest Famil. et des Accid. du Travail"),
        'salaireotal':fields.function(totalsalaire,""),
        'regimetotal':fields.function(totalregime,""),
        'travailtotal':fields.function(totaltravail,""),
        
        # saisie des champs du 2e tableau de la declaration CNPS:
        'pcprr1':fields.float(),
        'pcprr2':fields.float(),
        'ppqecp1':fields.float(),
        'ppqecp2':fields.float(),



        # saisie des champs du 3e tableau de la declaration CNPS:
        'pf1':fields.float(),
        'pf2':fields.float(),
        'pf3':fields.float("Cotisation due Prestations Familiales"),
        'at1':fields.float(),
        'at2':fields.float(),
        'at3':fields.float("Cotisation due Accidents du Travail"),
        'rr1':fields.float(),
        'rr2':fields.float(),
        'rr3':fields.float(string="Cotisation due Régime de Retraite"),
        'tcap':fields.float("TOTAL COTISATIONS A PAYER"),
        
    }


###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
######################################################               FDFP            ##############################################   

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
        'tauxtafdfp':fields.float(),
        'montantmensueltafdfp':fields.float("MONTANT MENSUEL TA"),
        'remunerationbttfcfp':fields.float(),
        'tauxtfcfdfp':fields.float(),
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



###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
######################################################               ITS            ##############################################

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

        # Determination de l'assiette

            # 1er tableau
        'montanttv1':fields.float(''),
        'effectif1':fields.float(""),
        'montantexo1':fields.float(""),
        'montanttax1':fields.float(""),
        'abattement1':fields.char(""),
        'revenuni1':fields.float(""),
        'montanttv2':fields.float(''),
        'effectif2':fields.float(""),
        'montantexo2':fields.float(""),
        'montanttax2':fields.float(""),
        'abattement2':fields.char(""),
        'revenuni2':fields.float(""),

            # 2e tableau
        'montanttv3':fields.float(''),
        'effectif3':fields.float(""),
        'montantexo3':fields.float(""),
        'montanttax3':fields.float(""),
        'abattement3':fields.char(""),
        'revenuni3':fields.float(""),
        'montanttv4':fields.float(''),
        'effectif4':fields.float(""),
        'montantexo4':fields.float(""),
        'montanttax4':fields.float(""),
        'abattement4':fields.char(""),
        'revenuni4':fields.float(""),

           # 3e tableau
        'montantrv':fields.float(''),
        'montantan':fields.float(""),
        'montanta':fields.float(""),
        'montanttb':fields.float("Montant total Revenu brut"),

           # 4e tableau
        'montantsalaires1':fields.float(''),
        'indemnite1':fields.float(""),
        'revenutotal1':fields.float(""),
        'revenunet1':fields.float(""),
        'montantsalaires2':fields.float(''),
        'indemnite2':fields.float(""),
        'revenutotal2':fields.float(""),
        'revenunet2':fields.float(""),

           # 5e tableau
        'totalmontantnet1':fields.float(""),
        'totalmontantnet2':fields.float(""),

        # Détermination de l'impot

        # impots retenus sur  les salaires
            # 1er tableau
        'base1':fields.float(""),
        'tauximpot1':fields.float(""),
        'montantimpot1':fields.float(""),
        'base2':fields.float(""),
        'tauximpot2':fields.float(""),
        'montantimpot2':fields.float(""),
        'base3':fields.float(""),
        'tauximpot3':fields.char(""),
        'montantimpot3':fields.float(""),

            # 2e tableau
        'totalrs':fields.float('TOTAL DES RETENUES AUX SALARIES'),
        # contributions a la charge de  l'employeur
            # 1er tableau
        'effectife1':fields.float(""),
        'revenuni1':fields.float(""),
        'touxe1':fields.float(""),
        'montante1':fields.float(""),
        'effectife2':fields.float(""),
        'revenuni2':fields.float(""),
        'touxe2':fields.float(""),
        'montante2':fields.float(""),
        'effectife3':fields.float(""),
        'revenuni3':fields.float(""),
        'touxe3':fields.float(""),
        'montante3':fields.float(""),
        'effectife4':fields.float(""),
        'revenuni4':fields.float(""),
        'touxe4':fields.float(""),
        'montante4':fields.float(""),
        'effectife5':fields.float(""),
        'revenuni5':fields.float(""),
        'touxe5':fields.float(""),
        'montante5':fields.float(""),
            # 2e tableau
        'totalcontribution':fields.float("TOTAL DES CONTRIBUTIONS A LA CHARGE DE L’EMPLOYEUR"),

            # 1er tableau ( impots retenu sur salaire)
            # retenue specifique du regime forestier en cas de fermage
        'revenunetimp':fields.float(""),
        'tauxre':fields.float(""),
        'montantretenu':fields.float(""),

            # regularisation

             #1er tableau
        'impots':fields.float(""),
        'contributionn':fields.float(""),
        'impotgsr':fields.float(""),
        'contributione':fields.float(""),
        'contributionnce':fields.float(""),
        'totalr':fields.float(""),
             # 2e tableau
        'montanttp':fields.float("MONTANT TOTAL A PAYER"),
        'montantr':fields.float("MONTAN A REPORTER"),
    }




###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
######################################################               TSE            ##############################################

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
        'tauxtse':fields.float('Taux'),
        'montanttaxetse':fields.float('Montant de la taxe'),
        'regulationtse':fields.float('Regulation'),
        'montantapayetse':fields.float('Montant de la taxe à payer'),
        'montantareportertse':fields.float('Montant à reporter'),
        
    }



###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
######################################################              TVA           ##############################################

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
        'tauxtvabrutea':fields.float("Taux"),
        "montannttvabrutea":fields.float("Montant"),
        'chiffreataxhttvabrutea':fields.float("Chiffre d'affaire taxable HT"),
        'tauxtvabrutea':fields.float("Taux"),
        "montannttvabrutea":fields.float("Montant"),
        'chiffreataxhttvabruteb':fields.float("Chiffre d'affaire taxable HT"),
        'tauxtvabruteb':fields.float("Taux"),
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

 

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
######################################             ETATS DES TAXES DEDUCTIBLES         ############################################

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
        'elementetat': fields.one2many('declaration.elementetat', 'element_id', 'Order Lines'),
    }




