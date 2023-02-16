from libraries.main.Main import Main
from robot.api.deco import not_keyword


tools = Main()

@not_keyword
def MyToken():
    '''
    This function reads global sheet which contains base url and token related information
    :return: It will return newly generated token and application base url
    '''
    global_settings = tools.read_conf(sheet_name='global')
    global_settings = global_settings[list(global_settings)[0]]
    token_url = global_settings['token_url']
    app_url = global_settings['api_base_url']
    headers = {"content-type": "application/x-www-form-urlencoded", "Accept-Charset": "UTF-8"}
    admin_data = dict(client_id=global_settings['client_id'], client_secret=global_settings['client_secret'],
                username=global_settings['admin_username'],
                password=global_settings['admin_password'], scope=global_settings['scope'],
                grant_type=global_settings['grant_type'])
    anonymous_data = dict(client_id=global_settings['client_id'], client_secret=global_settings['client_secret'],
                      username=global_settings['anonymous_username'],
                      password=global_settings['anonymous_password'], scope=global_settings['scope'],
                      grant_type=global_settings['grant_type'])
    customer_data = dict(client_id=global_settings['client_id'], client_secret=global_settings['client_secret'],
                      username=global_settings['customer_username'],
                      password=global_settings['customer_password'], scope=global_settings['scope'],
                      grant_type=global_settings['grant_type'])
    admin_token = tools.get_token(token_url=token_url, headers=headers, data=admin_data)
    anonymous_token = tools.get_token(token_url=token_url, headers=headers, data=anonymous_data)
    customer_token = tools.get_token(token_url=token_url, headers=headers, data=customer_data)

    return admin_token, app_url


@not_keyword
def ExtraTokens(user_type='anonymous'):
    '''
    This function reads global sheet which contains base url and token related information
    :return: It will return newly generated anonymous and customer tokens respectifully and application base url
    '''
    assert user_type in ['anonymous', 'customer'], 'user_type type parameter must be anonymous or customer'
    global_settings = tools.read_conf(sheet_name='global')
    global_settings = global_settings[list(global_settings)[0]]
    token_url = global_settings['token_url']
    app_url = global_settings['api_base_url']
    headers = {"content-type": "application/x-www-form-urlencoded", "Accept-Charset": "UTF-8"}
    data = dict(client_id=global_settings['client_id'], client_secret=global_settings['client_secret'],
                          username=global_settings[f'{user_type}_username'],
                          password=global_settings[f'{user_type}_password'], scope=global_settings['scope'],
                          grant_type=global_settings['grant_type'])

    token = tools.get_token(token_url=token_url, headers=headers, data=data)
    return token

@not_keyword
def ApiEndPoints() -> dict:
    '''
    Reads all the end points mentioned in end points sheet within main configuration file
    :return: All Application end points in dictionary
    '''
    api_end_points = tools.read_conf(sheet_name='endpoints')
    api_end_points = api_end_points[list(api_end_points)[0]]
    return api_end_points

# Below section will be used to set global variables

token, base_url = MyToken() # setting up token and base url variables
anonymous_token = ExtraTokens(user_type='anonymous')
customer_token = ExtraTokens(user_type='customer')
####################################################################################



# setting up all api end points variables
# Note ** --> Add All API points here in try section
all_api = ApiEndPoints()
try:

    create_new_api = all_api['create_new']
    create_category_api = all_api['create_category']
    update_category_api = all_api['update_category']
    get_category_by_id_api = all_api['get_category_by_id']
    patch_category_meta_api = all_api['patch_category_meta']
    patch_parentid_api = all_api['patch_parentid']
    create_child_category_api = all_api['create_child_category']
    get_all_categories_api = all_api['get_all_categories']
    get_by_categorycode_api = all_api['get_by_categorycode']
    get_by_childid_api = all_api['get_by_childid']
    get_by_parentid_api = all_api['get_by_parentid']
    get_category_by_type_api = all_api['get_category_by_type']
    get_category_by_dataversion_api = all_api['get_category_by_dataversion']
    get_category_root_api = all_api['get_category_root']
    get_category_by_criteria_api = all_api['get_category_by_criteria']
    delete_category_api = all_api['delete_category']
    create_pocategory_api = all_api['create_pocategory']
    update_pocategory_api = all_api['update_pocategory']
    create_child_pocategory_api = all_api['create_child_pocategory']
    create_resource_category_api = all_api['create_resource_category']
    update_resource_category_api = all_api['update_resource_category']
    create_child_resource_category_api = all_api['create_child_resource_category']
    get_productoffers_by_categoryid_api = all_api['get_productoffers_by_categoryid']
    get_offercontainer_category_api = all_api['get_offercontainer_category']
    create_service_category_api = all_api['create_service_category']
    update_service_category_api = all_api['update_service_category']
    create_child_service_category_api = all_api['create_child_service_category']
    get_lifecyclestatus_api = all_api['get_lifecyclestatus']
    get_entity_status_transition_detail_api = all_api['get_entity_status_transition_detail']

    create_mchar_api = all_api['create_mchar']
    update_mchar_api = all_api['update_mchar']
    get_characteristics_by_id_api = all_api['get_characteristics_by_id']
    delete_char_by_id_api = all_api['delete_char_by_id']
    create_import_characteristics_api = all_api['create_import_characteristics']
    get_characteristics_by_search_api = all_api['get_characteristics_by_search']
    get_characteristics_by_type_api = all_api['get_characteristics_by_type']

    create_service_spec_api = all_api['create_serviceSpec']
    update_service_spec_api = all_api['update_serviceSpec']
    get_serviceSpec_id_api = all_api['get_serviceSpec_id']
    patch_service_api = all_api['patch_service']
    patch_metaextensions_service_api = all_api['patch_metaextensions_service']
    import_serSpec_api = all_api['import_serSpec']
    get_serSpec_by_code_api = all_api['get_serSpec_by_code']
    get_serSpec_by_ver_id_api = all_api['get_serSpec_by_ver_id']
    get_serSpec_by_search_api = all_api['get_serSpec_by_search']
    get_by_serspec_objects_api = all_api['get_by_serspec_objects']

    create_resourceSpec_api = all_api['create_resourceSpec']
    update_resourceSpec_api = all_api['update_resourceSpec']
    get_resource_spec_by_id_api = all_api['get_resource_spec_by_id']
    patch_resource_api = all_api['patch_resource']
    delete_resourceSpec_api = all_api['delete_resourceSpec']
    import_resSpec_api = all_api['import_resSpec']
    patch_metaextensions_api = all_api['patch_metaextensions']
    get_resSpec_by_code_api = all_api['get_resSpec_by_code']
    get_resSpec_by_ver_id_api = all_api['get_resSpec_by_ver_id']
    get_resSpec_by_search_api = all_api['get_resSpec_by_search']
    get_by_resspec_objects_api = all_api['get_by_resspec_objects']

    create_productSpec_api = all_api['create_productSpec']
    update_productSpec_api = all_api['update_productSpec']
    get_resourceSpec_id_api = all_api['get_resourceSpec_id']
    patch_metaextensions_product_api = all_api['patch_metaextensions_product']
    patch_product_Spec_api = all_api['patch_product_Spec']
    delete_productSpec_api = all_api['delete_productSpec']
    import_ProSpec_api = all_api['import_ProSpec']
    get_proSpec_by_code_api = all_api['get_proSpec_by_code']
    get_proSpec_by_ver_id_api = all_api['get_proSpec_by_ver_id']
    get_proSpec_by_search_api = all_api['get_proSpec_by_search']
    get_by_prospec_objects_api = all_api['get_by_prospec_objects']
    # create_resource_candidate = all_api['create_resource_candidate']
    # create_service_candidate = all_api['create_service_candidate']

    ################TAX###############################
    create_tax_api = all_api['create_tax']
    update_tax_api = all_api['update_tax']
    delete_tax_api = all_api['delete_tax']
    get_tax_by_id_api = all_api['get_tax_by_id']
    get_all_tax_api = all_api['get_all_tax']
    get_tax_by_filters_api = all_api['get_tax_by_filters']


    #********************Catalog*************************
    create_catalog_api = all_api['create_catalog']
    delete_catalog_api = all_api['delete_catalog']
    patch_catalog_lifecyclestatus_api = all_api['patch_catalog_lifecyclestatus']
    Get_Catalog = all_api['Get_Catalog']
    Get_Catalog_Id = all_api['Get_Catalog_Id']
    Get_Catalog_Code = all_api['Get_Catalog_Code']
    Get_Catalog_Name = all_api['Get_Catalog_Name']
    Get_Catalog_Type = all_api['Get_Catalog_Type']
    Get_Catalog_Search = all_api['Get_Catalog_Search']

    #******************Product Offer**********************
    Create_product_Offer_api = all_api['Create_product_Offer']
    Delete_Product_Offer = all_api['Delete_Product_Offer']
    Patch_PO_LCS_Direct = all_api['Patch_PO_LCS_Direct']
    Patch_Product_Offer = all_api['Patch_Product_Offer']
    patch_po_metadata_api = all_api['patch_po_metadata']
    get_all_po_api = all_api['get_all_po']
    get_by_id_and_version = all_api['get_by_id_and_version']
    get_po_by_id_api = all_api['get_po_by_id']
    get_po_by_dataversion_api = all_api['get_po_by_dataversion']
    get_po_by_code_api = all_api['get_po_by_code']
    get_po_by_name_api = all_api['get_po_by_name']
    get_po_by_criteria_api = all_api['get_po_by_criteria']

    # ******************POP**********************
    create_pop_api = all_api['create_pop']
    update_pop_api = all_api['update_pop']
    get_pop_by_id_api = all_api['get_pop_by_id']
    delete_pop_by_id_api = all_api['delete_pop_by_id']
    patch_pop_api = all_api['patch_pop']
    get_all_pop_api = all_api['get_all_pop']
    get_pop_dataversion_api = all_api['get_pop_dataversion']
    get_pop_by_lifecyclestatus_api = all_api['get_pop_by_lifecyclestatus']
    get_by_criteria_api = all_api['get_by_criteria']


    # ******************PROMOTIONACTION**********************
    create_promotionaction_api = all_api['create_promotionaction']
    update_promotionaction_api = all_api['update_promotionaction']
    delete_promotionaction_api = all_api['delete_promotionaction']
    get_promotionaction_by_id_api = all_api['get_promotionaction_by_id']
    get_all_promotionaction_api = all_api['get_all_promotionaction']
    get_promotionaction_by_filters_api = all_api['get_promotionaction_by_filters']

    # ******************Prciepoint**********************
    create_pp_api = all_api['create_pp']
    update_pp_api = all_api['update_pp']
    delete_pp_api = all_api['delete_pp']
    get_pp_by_id_api = all_api['get_pp_by_id']
    get_all_pp_api = all_api['get_all_pp']
    get_pp_by_filters_api = all_api['get_pp_by_filters']

    # ******************Promotions**********************
    create_promotion_api = all_api['create_promotion']
    update_promotion_api=all_api['update_promotion']
    get_promotion_by_id=all_api['get_promotion_by_id']
    get_promotion_by_code=all_api['get_promotion_by_code']
    search_promotion=all_api['search_promotion']
    delete_promotion_by_id=all_api['delete_promotion_by_id']
    change_promotion_staus=all_api['change_status']
    import_promotion=all_api['import_promotion']
    meta_extension_promotion=all_api['meta_extension_promotion']

    create_rule_api = all_api['create_rule']
    update_rule_api = all_api['update_rule']
    get_rule_by_id_api = all_api['get_rule_by_id']
    delete_rule_api = all_api['delete_rule']
    get_all_rule_api = all_api['get_all_rule']
    get_rule_by_categoryid_api = all_api['get_rule_by_categoryid']
    get_rule_by_productid_api = all_api['get_rule_by_productid']
    get_rule_by_promoid_api = all_api['get_rule_by_promoid']
    get_rule_by_recommendationid_api = all_api['get_rule_by_recommendationid']
    get_rule_by_region_api = all_api['get_rule_by_region']
    get_rule_by_ruleType_api = all_api['get_rule_by_ruleType']
    get_rule_by_advancequery_api = all_api['get_rule_by_advancequery']
    create_comp_rule_api = all_api['create_rule']
    update_comp_rule_api = all_api['update_rule']
    create_sc_rule_api = all_api['create_rule']
    update_sc_rule_api = all_api['update_rule']
    create_promo_rule_api = all_api['create_rule']
    update_promo_rule_api = all_api['update_rule']
    create_reco_rule_api = all_api['create_rule']
    update_reco_rule_api = all_api['update_rule']
    create_compspecialchar_rule_api = all_api['create_rule']


    create_stock_api = all_api['create_stock']
    update_stock_api = all_api['update_stock']
    delete_stock_api = all_api['delete_stock']
    get_stock_by_id_api = all_api['get_stock_by_id']
    get_all_stock_api = all_api['get_all_stock']
    get_stock_by_filter_api = all_api['get_stock_by_filter']
    patch_stock_api = all_api['patch_stock']

    create_recommendation_api = all_api['create_recommendation']
    update_recommendation_api = all_api['update_recommendation']
    get_all_recommendations_api = all_api['get_all_recommendations']
    get_recommendation_by_id_api = all_api['get_recommendation_by_id']
    delete_recommendation_api = all_api['delete_recommendation']
    get_recommendation_by_type_api = all_api['get_recommendation_by_type']

    # ******************RecommendationBulk**********************
    create_rsc_api = all_api['create_rsc']
    create_bulk_recommendation_api = all_api['create_bulk_recommendation']


except KeyError as e:
    print(f"Key {e} not found in Configuration Excl's Endpoint worksheet")


# print(f'Admin Token is {token}')
# print(f'Anonymous Token is {anonymous_token}')
# print(f'Customer Token is {customer_token}')


