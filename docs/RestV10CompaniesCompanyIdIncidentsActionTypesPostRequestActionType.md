# RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType

Incident Action Type object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Incident Action Type | 
**active** | **bool** | Flag that denotes if the Incident Action Type is available for use | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_post_request_action_type import RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType from a JSON string
rest_v10_companies_company_id_incidents_action_types_post_request_action_type_instance = RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType.to_json())

# convert the object into a dict
rest_v10_companies_company_id_incidents_action_types_post_request_action_type_dict = rest_v10_companies_company_id_incidents_action_types_post_request_action_type_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType from a dict
rest_v10_companies_company_id_incidents_action_types_post_request_action_type_from_dict = RestV10CompaniesCompanyIdIncidentsActionTypesPostRequestActionType.from_dict(rest_v10_companies_company_id_incidents_action_types_post_request_action_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


