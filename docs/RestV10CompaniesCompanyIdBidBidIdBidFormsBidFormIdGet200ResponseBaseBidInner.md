# RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner

Base Bid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Bid Form Title | [optional] 
**position** | **int** | Position | [optional] 
**header** | **bool** | Whether the item is a header or not | [optional] 
**bid_form_items** | [**List[RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner]**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerBidFormItemsInner.md) |  | [optional] 
**sub_sections** | [**List[RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner]**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner from a JSON string
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_instance = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_dict = rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner from a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_from_dict = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner.from_dict(rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


