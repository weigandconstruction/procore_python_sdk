# RestV10CompaniesCompanyIdTimecardEntriesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Timecard Entry belongs to | 
**timecard_entry** | [**TimecardEntry4**](TimecardEntry4.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_post_request import RestV10CompaniesCompanyIdTimecardEntriesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdTimecardEntriesPostRequest from a JSON string
rest_v10_companies_company_id_timecard_entries_post_request_instance = RestV10CompaniesCompanyIdTimecardEntriesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdTimecardEntriesPostRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_timecard_entries_post_request_dict = rest_v10_companies_company_id_timecard_entries_post_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdTimecardEntriesPostRequest from a dict
rest_v10_companies_company_id_timecard_entries_post_request_from_dict = RestV10CompaniesCompanyIdTimecardEntriesPostRequest.from_dict(rest_v10_companies_company_id_timecard_entries_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


