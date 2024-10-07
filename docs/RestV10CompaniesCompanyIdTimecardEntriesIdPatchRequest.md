# RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Timecard Entry belongs to | 
**timecard_entry** | [**TimecardEntry5**](TimecardEntry5.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_id_patch_request import RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest from a JSON string
rest_v10_companies_company_id_timecard_entries_id_patch_request_instance = RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_timecard_entries_id_patch_request_dict = rest_v10_companies_company_id_timecard_entries_id_patch_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest from a dict
rest_v10_companies_company_id_timecard_entries_id_patch_request_from_dict = RestV10CompaniesCompanyIdTimecardEntriesIdPatchRequest.from_dict(rest_v10_companies_company_id_timecard_entries_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


