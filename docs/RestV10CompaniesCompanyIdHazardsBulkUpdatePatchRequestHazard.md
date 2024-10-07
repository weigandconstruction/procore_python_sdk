# RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard

IDs of all Hazards specified for bulk update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**active** | **bool** | Flag that denotes if the Hazards are available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_hazards_bulk_update_patch_request_hazard import RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard from a JSON string
rest_v10_companies_company_id_hazards_bulk_update_patch_request_hazard_instance = RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard.to_json())

# convert the object into a dict
rest_v10_companies_company_id_hazards_bulk_update_patch_request_hazard_dict = rest_v10_companies_company_id_hazards_bulk_update_patch_request_hazard_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard from a dict
rest_v10_companies_company_id_hazards_bulk_update_patch_request_hazard_from_dict = RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequestHazard.from_dict(rest_v10_companies_company_id_hazards_bulk_update_patch_request_hazard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


