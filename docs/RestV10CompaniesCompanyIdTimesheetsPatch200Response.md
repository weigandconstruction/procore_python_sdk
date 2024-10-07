# RestV10CompaniesCompanyIdTimesheetsPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_timecard_entries** | [**List[TimecardEntry2]**](TimecardEntry2.md) | Array of updated timecard entries | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_timesheets_patch200_response import RestV10CompaniesCompanyIdTimesheetsPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdTimesheetsPatch200Response from a JSON string
rest_v10_companies_company_id_timesheets_patch200_response_instance = RestV10CompaniesCompanyIdTimesheetsPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdTimesheetsPatch200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_timesheets_patch200_response_dict = rest_v10_companies_company_id_timesheets_patch200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdTimesheetsPatch200Response from a dict
rest_v10_companies_company_id_timesheets_patch200_response_from_dict = RestV10CompaniesCompanyIdTimesheetsPatch200Response.from_dict(rest_v10_companies_company_id_timesheets_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


