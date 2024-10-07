# Lookahead1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Lookahead start date, in project time zone | 
**end_date** | **str** | Lookahead end date, in project time zone | 
**copied_from_id** | **int** | ID of a previously created lookahead that will be used to populate this lookahead. Defaults to the most recent lookahead. | [optional] 

## Example

```python
from procore_sdk.models.lookahead1 import Lookahead1

# TODO update the JSON string below
json = "{}"
# create an instance of Lookahead1 from a JSON string
lookahead1_instance = Lookahead1.from_json(json)
# print the JSON string representation of the object
print(Lookahead1.to_json())

# convert the object into a dict
lookahead1_dict = lookahead1_instance.to_dict()
# create an instance of Lookahead1 from a dict
lookahead1_from_dict = Lookahead1.from_dict(lookahead1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


