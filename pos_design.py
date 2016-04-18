import sqlite3
import types
class pos_model:
    def get_product_list(self,tablename):
        ''' this function will return all the produts available ij the store'''
        query = "selct p_name from '%s' " %tablename
        product_list=self._dbselect(query)
        products=[]
        for row in product_list:
            products.append(row[0])
        return products

    def get_product_size(self,p_name):
        '''this function will return size of the product'''
        query=" select size(oz) from products where p_name ='%s' " %p_name
        size=self._dbselect(query)
        for row in size:
            return row[0]
    
    def get_profit(self,p_id):
        ''' this function will return the profit of the particuler product'''
        query=" select profit from profit where product_id ='%s' " %p_id
        profit=self._dbselect(query)
        for row in profit:
            return (row[0])
        
    def _dbselect(self,query):
        connection = sqlite3.connect('pos')
        cursorObj = connection.cursor()
        results = cursorObj.execute(query)
        connection.commit()
        cursorObj.close()
        return results

class pos_view:
    def product_list(self,products):
        print('####All Product available in the store###')
        for item in products:
            print(item)
    def product_size(self,p_name,size):
        print("####The size of the %s is %d ###"%(p_name,size))
        
    def profit(self,p_id,profit):
        print("### The profit of the item is %s ###"%profit)

class pos_controler:
    def __init__(self):
        pass
    def getProductList(self,tablename):
        model=pos_model()
        view=pos_view()
        list_data=model.get_product_list(table_name)
        return view.product_list(list_data)
    
    def getSize(self,p_name):
        model=pos_model()
        view=pos_view()
        out=model.get_product_size(p_name)
        return view.product_size(p_name,out)
        
    def getProfit(self,p_id):
        model=pos_model()
        view=pos_view()
        data=model.get_profit(p_id)
        return view.profit(p_id,data)
    
        
        
        
