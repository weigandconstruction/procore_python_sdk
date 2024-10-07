# RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hazard** | [**RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard**](RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_hazards_bulk_update_patch_request import RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest from a JSON string
rest_v10_companies_company_id_hazards_bulk_update_patch_request_instance = RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_hazards_bulk_update_patch_request_dict = rest_v10_companies_company_id_hazards_bulk_update_patch_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest from a dict
rest_v10_companies_company_id_hazards_bulk_update_patch_request_from_dict = RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest.from_dict(rest_v10_companies_company_id_hazards_bulk_update_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


