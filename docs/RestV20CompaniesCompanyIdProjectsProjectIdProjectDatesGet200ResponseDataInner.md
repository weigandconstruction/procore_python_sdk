# RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Project Date Id | [optional] 
**project_membership_id** | **str** | Project Date Membership. The project date membership id associates a project date with an existing project. | [optional] 
**name** | **str** | Project Date Name | [optional] 
**var_date** | **str** | Project Date Date | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_project_dates_get200_response_data_inner import RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner from a JSON string
rest_v20_companies_company_id_projects_project_id_project_dates_get200_response_data_inner_instance = RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_project_dates_get200_response_data_inner_dict = rest_v20_companies_company_id_projects_project_id_project_dates_get200_response_data_inner_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner from a dict
rest_v20_companies_company_id_projects_project_id_project_dates_get200_response_data_inner_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200ResponseDataInner.from_dict(rest_v20_companies_company_id_projects_project_id_project_dates_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


