# RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner

Alternate Bid

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
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_alternates_inner import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner from a JSON string
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_alternates_inner_instance = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_alternates_inner_dict = rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_alternates_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner from a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_alternates_inner_from_dict = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner.from_dict(rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_alternates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


