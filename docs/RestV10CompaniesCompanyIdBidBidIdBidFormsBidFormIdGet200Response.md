# RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response

Bid Form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Bid Form Title | [optional] 
**base_bid** | [**List[RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner]**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInner.md) |  | [optional] 
**alternates** | [**List[RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner]**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseAlternatesInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response from a JSON string
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_instance = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_dict = rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response from a dict
rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_from_dict = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.from_dict(rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


