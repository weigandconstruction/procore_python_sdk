# CompanyObservationTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_id** | **int** | The ID of the Company Observation Template&#39;s Trade | [optional] 

## Example

```python
from procore_sdk.models.company_observation_template import CompanyObservationTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyObservationTemplate from a JSON string
company_observation_template_instance = CompanyObservationTemplate.from_json(json)
# print the JSON string representation of the object
print(CompanyObservationTemplate.to_json())

# convert the object into a dict
company_observation_template_dict = company_observation_template_instance.to_dict()
# create an instance of CompanyObservationTemplate from a dict
company_observation_template_from_dict = CompanyObservationTemplate.from_dict(company_observation_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


