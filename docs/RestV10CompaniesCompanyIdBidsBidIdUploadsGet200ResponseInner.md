# RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner

Bid Upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Created at | [optional] 
**name** | **str** | Bid Upload file name | [optional] 
**expired** | **bool** | Bid Upload is expired | [optional] 
**links** | [**RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInnerLinks**](RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInnerLinks.md) |  | [optional] 
**id** | **int** | Upload ID | [optional] 
**uuid** | **str** | UUID | [optional] 
**url** | **str** | URL of the storage | [optional] 
**fields** | [**RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInnerFields**](RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInnerFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner import RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner_instance = RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner_dict = rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner from a dict
rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner_from_dict = RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner.from_dict(rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


