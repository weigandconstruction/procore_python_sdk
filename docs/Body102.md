# Body102


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**standard_cost_code_list_id** | **int** | Standard Cost Code List ID | 
**standard_cost_code** | [**StandardCostCode1**](StandardCostCode1.md) |  | 

## Example

```python
from procore_sdk.models.body102 import Body102

# TODO update the JSON string below
json = "{}"
# create an instance of Body102 from a JSON string
body102_instance = Body102.from_json(json)
# print the JSON string representation of the object
print(Body102.to_json())

# convert the object into a dict
body102_dict = body102_instance.to_dict()
# create an instance of Body102 from a dict
body102_from_dict = Body102.from_dict(body102_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


