# RestV10CompaniesCompanyIdProgramsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Program ID | [optional] 
**name** | **str** | Program name | [optional] 
**address_freeform** | **str** | Program address | [optional] 
**website** | **str** | Program website | [optional] 
**zip** | **str** | Program zip-code | [optional] 
**longitude** | **str** | Program longitude | [optional] 
**latitude** | **str** | Program latitude | [optional] 
**projects** | [**List[RestV10CompaniesCompanyIdProgramsPost201ResponseAllOfProjectsInner]**](RestV10CompaniesCompanyIdProgramsPost201ResponseAllOfProjectsInner.md) | Array of program projects | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_programs_post201_response import RestV10CompaniesCompanyIdProgramsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdProgramsPost201Response from a JSON string
rest_v10_companies_company_id_programs_post201_response_instance = RestV10CompaniesCompanyIdProgramsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdProgramsPost201Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_programs_post201_response_dict = rest_v10_companies_company_id_programs_post201_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdProgramsPost201Response from a dict
rest_v10_companies_company_id_programs_post201_response_from_dict = RestV10CompaniesCompanyIdProgramsPost201Response.from_dict(rest_v10_companies_company_id_programs_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


