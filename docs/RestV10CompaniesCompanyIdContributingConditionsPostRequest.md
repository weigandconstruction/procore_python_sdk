# RestV10CompaniesCompanyIdContributingConditionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributing_condition** | [**RestV10CompaniesCompanyIdContributingConditionsPostRequestContributingCondition**](RestV10CompaniesCompanyIdContributingConditionsPostRequestContributingCondition.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_contributing_conditions_post_request import RestV10CompaniesCompanyIdContributingConditionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdContributingConditionsPostRequest from a JSON string
rest_v10_companies_company_id_contributing_conditions_post_request_instance = RestV10CompaniesCompanyIdContributingConditionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdContributingConditionsPostRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_contributing_conditions_post_request_dict = rest_v10_companies_company_id_contributing_conditions_post_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdContributingConditionsPostRequest from a dict
rest_v10_companies_company_id_contributing_conditions_post_request_from_dict = RestV10CompaniesCompanyIdContributingConditionsPostRequest.from_dict(rest_v10_companies_company_id_contributing_conditions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


