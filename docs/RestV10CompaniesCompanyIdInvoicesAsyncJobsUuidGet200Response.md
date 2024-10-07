# RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response

An Invoicing Async Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Async Job | [optional] 
**company_id** | **int** | Company ID | [optional] 
**created_by_id** | **int** | LoginInformation ID that created the Async Job | [optional] 
**status** | **str** | Status of the Async Job | [optional] 
**result** | [**RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult**](RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of Async Job creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Async Job | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response import RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response from a JSON string
rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response_instance = RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response_dict = rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response from a dict
rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response_from_dict = RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response.from_dict(rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


