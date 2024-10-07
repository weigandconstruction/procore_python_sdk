# Body101


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**standard_cost_code_list** | [**Body101StandardCostCodeList**](Body101StandardCostCodeList.md) |  | 

## Example

```python
from procore_sdk.models.body101 import Body101

# TODO update the JSON string below
json = "{}"
# create an instance of Body101 from a JSON string
body101_instance = Body101.from_json(json)
# print the JSON string representation of the object
print(Body101.to_json())

# convert the object into a dict
body101_dict = body101_instance.to_dict()
# create an instance of Body101 from a dict
body101_from_dict = Body101.from_dict(body101_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


