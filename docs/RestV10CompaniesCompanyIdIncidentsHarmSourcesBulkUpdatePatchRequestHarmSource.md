# RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource

IDs of all Harm Sources specified for bulk update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**active** | **bool** | Flag that denotes if the Harm Sources are available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request_harm_source import RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource from a JSON string
rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request_harm_source_instance = RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request_harm_source_dict = rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request_harm_source_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource from a dict
rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request_harm_source_from_dict = RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequestHarmSource.from_dict(rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request_harm_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


