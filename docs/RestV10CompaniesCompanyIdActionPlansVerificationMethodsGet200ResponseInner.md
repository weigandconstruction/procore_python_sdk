# RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**active** | **bool** | Specifies if the Action Plan Verification Method is intended for use | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**name** | **str** | Name | [optional] 
**source_key** | **str** | Internal translation key | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner import RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner_instance = RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner_dict = rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner from a dict
rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner_from_dict = RestV10CompaniesCompanyIdActionPlansVerificationMethodsGet200ResponseInner.from_dict(rest_v10_companies_company_id_action_plans_verification_methods_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


