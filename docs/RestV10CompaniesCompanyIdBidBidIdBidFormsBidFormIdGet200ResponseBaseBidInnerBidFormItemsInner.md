# RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner

Bid Form Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**cost_code** | [**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInnerCostCode**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInnerCostCode.md) |  | [optional] 
**description** | **str** | Bid Form Item Description | [optional] 
**position** | **int** | Position | [optional] 
**subject** | **str** | Subject for Plain Text Items | [optional] 
**item_type** | **str** | Bid Form Items can be of various types. This property does determine which one is used. | [optional] 
**response_type** | **str** | Bid Form Items can have various response types. This property determines which one is used. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_bid_form_items_inner import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner from a JSON string
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_bid_form_items_inner_instance = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_bid_form_items_inner_dict = rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_bid_form_items_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner from a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_bid_form_items_inner_from_dict = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner.from_dict(rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_bid_form_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


