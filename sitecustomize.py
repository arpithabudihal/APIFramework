import site
import os



# Setting up Project Base Dir
import sys

curdir = 'D:\\Catalog'
# curdir = os.getcwd()
print(f"Framework's Base Location being used is {curdir}")
print ('Catalog Management TestCase Execution Starting.Please Wait....')


# Adding new Customized Site Packages
site.addsitedir(curdir)
site.addsitedir(curdir+'\\Data')
site.addsitedir(curdir+'\\libraries')
site.addsitedir(curdir+'\\libraries\\MChar')
site.addsitedir(curdir+'\\libraries\\ServiceSpec')
site.addsitedir(curdir+'\\libraries\\ProductSpec')
site.addsitedir(curdir+'\\libraries\\Pmetaext')
site.addsitedir(curdir+'\\libraries\\Tax')
site.addsitedir(curdir+'\\libraries\\Catalog')
site.addsitedir(curdir+'\\libraries\\Category')
site.addsitedir(curdir+'\\libraries\\P1Category')
site.addsitedir(curdir+'\\libraries\\Product_Offer')
site.addsitedir(curdir+'\\libraries\\POP')
site.addsitedir(curdir+'\\libraries\\Promotions')
site.addsitedir(curdir+'\\libraries\\PromotionAction')
site.addsitedir(curdir+'\\libraries\\Pricepoint')
site.addsitedir(curdir+'\\libraries\\Rule')
site.addsitedir(curdir+'\\libraries\\RuleComp')
site.addsitedir(curdir+'\\libraries\\RulePromo')
site.addsitedir(curdir+'\\libraries\\RuleReco')
site.addsitedir(curdir+'\\libraries\\RuleSC')
site.addsitedir(curdir+'\\libraries\\StockManagement')
site.addsitedir(curdir+'\\libraries\\Recommendation')
site.addsitedir(curdir+'\\libraries\\RSC')
# print(sys.path)

