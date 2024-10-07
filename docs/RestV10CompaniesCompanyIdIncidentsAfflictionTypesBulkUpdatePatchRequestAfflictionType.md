# RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType

IDs of all Affliction Types specified for bulk update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**active** | **bool** | Flag that denotes if the Affliction Types are available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request_affliction_type import RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType from a JSON string
rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request_affliction_type_instance = RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request_affliction_type_dict = rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request_affliction_type_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType from a dict
rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request_affliction_type_from_dict = RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequestAfflictionType.from_dict(rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request_affliction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


